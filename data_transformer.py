import pandas as pd
import pg_helper
import matplotlib.pyplot as plt
import seaborn as sns

def transform_data():
    cur, conn = pg_helper.open_connect_to_db()
    cur.execute('select * from test_bs')
    raw_sql_list = cur.fetchall()
    raw_df = pd.DataFrame(raw_sql_list)
    raw_df.rename({0 : 'id', 1 : 'datetime', 2 : 'bs_measure'}, axis=1, inplace=True)
    trimmed_df = raw_df[['datetime','bs_measure']]
    trimmed_df.set_index('datetime',inplace=True)
    return trimmed_df