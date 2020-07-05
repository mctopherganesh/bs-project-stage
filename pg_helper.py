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
    table = """
    create table test_bs (
        id integer not null,
        date_time varchar(25) not null,
        blood_sugar numeric not null
    )
    """
    cur,conn = open_connect_to_db()
    
    cur.execute(table)
    conn.commit()
    cur.close()


def load_csv_data():
    cur, conn = open_connect_to_db()
    with open('blood_sugar_dataframe.csv','r') as f:
        next(f)
        cur.copy_from(f, 'test_bs', sep=',')

    conn.commit()
    cur.close()

def return_table_data():
    cur, conn = open_connect_to_db()
    cur.execute('select * from test_bs')
    print(cur.fetchall(), flush=True)
    close_connect_to_db(cur, conn)

def drop_old_table():
    cur, conn = open_connect_to_db()
    drop_statement = """drop table bs_test_table"""
    cur.execute(drop_statement)
    conn.commit()
    cur.close()



   
