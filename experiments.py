import pandas as pd
from datasets import load_dataset
from sqlalchemy import create_engine

# dataset = load_dataset('wikimedia/wikipedia', '20231101.uz')
#
# df = pd.DataFrame(dataset['train']).drop(columns=['id', 'url'])
#
# df = df.rename(columns={'title': 'query', 'text': 'answer'})
#
# engine = create_engine('postgresql+psycopg2://jointbert_user:bert_user@localhost/jointbert_base')
#
# df[['query', 'answer']].to_sql('app_qa', engine, if_exists='append', index=False)
