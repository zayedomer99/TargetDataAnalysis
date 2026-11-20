import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
password=quote_plus('Zayed2004.')
engine=create_engine(f'mysql+pymysql://root:{password}@localhost:3306/EcommerceDA')

list_csvs=[
    ('customers','customers.csv'),
    ('geolocation','geolocation.csv'),
    ('order_items','order_items.csv'),
    ('orders','orders.csv'),
    ('payments','payments.csv'),
    ('products','products.csv'),
    ('sellers','sellers.csv')
]
for table,file in list_csvs:
    filepath=f"./Files/{file}"
    df = pd.read_csv(filepath)
    df.to_sql(
        name=table,
        con=engine, 
        if_exists='replace',
        index=False
    )
    print(f"imported {file} successfully into {table}")
engine.dispose()

