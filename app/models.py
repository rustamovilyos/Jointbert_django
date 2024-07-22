from django.db import models


class QA(models.Model):
    query = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.query

    class Meta:
        verbose_name = 'Question-Answer'
        verbose_name_plural = 'Questions-Answers'
