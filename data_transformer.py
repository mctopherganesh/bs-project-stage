import pandas as pd
import pg_helper
import matplotlib.pyplot as plt
import seaborn as sns

def datestamp():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    cst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
    a = cst_now.strftime("%Y-%m-%d %H:%M:%S")
    a = a[5:]
    b = a[6:11]
    a = a[:5]
    b = b.replace(':','')
    a = a.replace('-','_')
    return a + '_' + b


def transform_data():
    cur, conn = pg_helper.open_connect_to_db()
    cur.execute('select * from bs_test')
    raw_sql_list = cur.fetchall()
    df = pd.DataFrame(raw_sql_list)
    df.rename({0 : 'datetime', 1 : 'bs_measure'}, axis=1, inplace=True)
    df.set_index('datetime',inplace=True)
    return df

def return_dist_plot():
    test_df = transform_data()
    sns.distplot(test_df['bs_measure'], vertical=True)
    filepath_w_datestamp = 'img/dist_plot_{}.png'.format(datestamp())
    plt.savefig(filepath_w_datestamp)
    return filepath_w_datestamp