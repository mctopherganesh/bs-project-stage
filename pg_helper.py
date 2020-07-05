import os
import psycopg2

db_url = os.environ['DATABASE_URL']

def open_connect_to_db():
    conn = psycopg2.connect(db_url, sslmode='require')
    cursor = conn.cursor()
    return cursor, conn
    
def close_connect_to_db(cursor, conn):    
    cursor.close()
    conn.close()

def create_table():
    tables = """
    create table test_bs (
        date_time varchar(25)
        blood_sugar integer not null
    )
    """,
    """
    create table test_food (
        date_time varchar(25) not null,
        food varchar(255) not null
    )
    """
    cur,conn = open_connect_to_db()
    for table in tables:
        cur.execute(table)
    cur.close()
    conn.commit()

def return_table_data():
    cur, conn = open_connect_to_db()
    cur.execute('select * from test_bs')
    close_connect_to_db(cur, conn)




   
