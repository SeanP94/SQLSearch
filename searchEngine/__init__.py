import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Connect to the PostgreSQL database server
conn_string = 'postgresql://postgres:dockerpw123@localhost/searchEngineTest'
engine = create_engine(conn_string)


conn = engine.connect()


createTable = """
CREATE TABLE IF NOT EXISTS productDB (
  Rank         INT   PRIMARY KEY       NOT NULL,
  Name         TEXT                    NOT NULL,
  Platform     TEXT                    NOT NULL,
  Year         INT                     NOT NULL,
  Genre        TEXT                    NOT NULL,
  Publisher    TEXT                    NOT NULL,
  NA_Sales     TEXT                    NOT NULL,
  JP_Sales     TEXT                    NOT NULL,
  Other_Sales  TEXT                    NOT NULL,
  Global_Sales TEXT                    NOT NULL
);
"""

df = pd.read_csv('data/vgsales.csv')
df.to_sql('products', con=conn, if_exists='replace', index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
query = 'select * from products'
cursor = conn.cursor()
cursor.execute(query)

for row in cursor.fetchall():
    print(row)