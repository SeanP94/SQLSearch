import psycopg2

# Connect to the PostgreSQL database server

postgresConnection = psycopg2.connect(
    host='localhost',
    port=5432,
    database='searchEngineTest',
    user='postgres',
    password='dockerpw123'
)
 
# Get cursor object from the database connection

cursor = postgresConnection.cursor()
