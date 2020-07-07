import pandas as pd
import pg_helper
import matplotlib.pyplot as plt
import seaborn as sns
import pytz
import datetime

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
    filepath_w_datestamp = 'img/distplot_{}.png'.format(datestamp())
    plt.savefig(filepath_w_datestamp)
    return filepath_w_datestamp

def return_line_plot_of_last(x):
    df = transform_data()
    df = df.tail(x)
    df = df.reset_index()
    df['datetime'] = df['datetime'].str.slice(start=5, stop=-3)
    ax = sns.pointplot(x='datetime', y='bs_measure', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    
    filepath_w_datestamp = 'img/lineplot_{}.png'.format(datestamp())
    plt.savefig(filepath_w_datestamp)
    plt.clf()
    return filepath_w_datestamp
    