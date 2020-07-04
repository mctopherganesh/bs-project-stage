import os
import psycopg2

db_url = os.environ['heroku_db_url']


conn = psycopg2.connect(db_url, sslmode='require')
cursor = conn.cursor()
print('connected tp ' + cursor.fetchone())
cursor.close()
conn.close()


   
