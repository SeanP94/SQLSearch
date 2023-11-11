import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Connect to the PostgreSQL database server
conn_string = 'postgresql://postgres:dockerpw123@localhost:5432/searchEngineTest'
engine = create_engine(conn_string)

# Load the CSV file into postgres 
conn = engine.connect()
df = pd.read_csv('~/SQLSearch/data/vgsales.csv')
df.to_sql('products', con=conn, if_exists='replace', index=False)

# SQLALCHEMY Connection
conn = psycopg2.connect(conn_string)
conn.autocommit = True




# Final cusor
cursor = conn.cursor()

def getProducts(min=None):
    '''Simply prints the tuples of all values; optional input for a limit on the amount'''
    query = 'select "Name" from products'
    if min:
        query += f" LIMIT {min}"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def searchForGame(userInput=''):
    ''' Uses full text search to search the database; Must input data'''
    userInput = userInput.replace(' ', '_')
    query = f"""
    SELECT
        *
    FROM
        products as p
    WHERE
        to_tsvector("Name") @@ to_tsquery('{userInput}');
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
