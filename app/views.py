from .models import QA
from .serializers import QASerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class QADetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QA.objects.all()
    serializer_class = QASerializer


class QAListCreateView(generics.ListCreateAPIView):
    queryset = QA.objects.all()
    serializer_class = QASerializer


@api_view(['GET', 'POST'])
def qa_list(request):
    if request.method == "GET":
        qa = QA.objects.all()
        serializer = QASerializer(qa, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = QASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def qa_detail(request, pk):
    try:
        qa = QA.objects.get(pk=pk)
    except QA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = QASerializer(qa)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = QASerializer(qa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        qa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
