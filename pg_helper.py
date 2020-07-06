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

def enter_bs_row(bs,dtsmp):
    cur, conn = open_connect_to_db()
    insert_statement = """insert into bs_test(datestamp, bs_measure)
                          values ({}, {});""".format(bs, dtsmp)
    cur.execute(insert_statement)

def create_table():
    table = """
    create table bs_test (
        datetime varchar(25) not null,
        bs_measure numeric not null
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
        cur.copy_from(f, 'bs_test', sep=',')

    conn.commit()
    cur.close()

def return_table_data():
    cur, conn = open_connect_to_db()
    cur.execute('select * from bs_test')
    print(cur.fetchall(), flush=True)
    close_connect_to_db(cur, conn)

def return_last_five():
    cur, conn = open_connect_to_db()
    cur.execute('select * from bs_test order by datetime limit 5 desc;')
    return cur.fetchall()

def drop_old_table():
    cur, conn = open_connect_to_db()
    drop_statement = """drop table bs_test"""
    cur.execute(drop_statement)
    conn.commit()
    cur.close()


# table names 
# test_bs as of 07/06/2020
# using bs_test for the update
   
