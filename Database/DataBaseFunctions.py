'''
Reusable Calculating Function for MySql Date
'''


import mysql.connector as mysql
import datetime


def length_calculator_db(table, ts_code, fromdate, todate):
    """
    calcualte bar size of stock data set
    Args:
        table (str): table name 
        ts_code (str): stock code 
        start_time (str): start datetime of backtesting
        end_time (str): end datetime of backtesting
    return:
        data (int): the length of stock dataset
    """
    start_time = datetime.datetime.strftime(fromdate, '%Y%m%d')
    end_time = datetime.datetime.strftime(todate, '%Y%m%d')

    db = mysql.connect(
        host="localhost",
        user="root",
        password="201202@",
        database="AStockMarket"
    )

    cur = db.cursor()
    sql = cur.execute(
        f"SELECT count(close) FROM {table} WHERE trade_date >= '{start_time}' and trade_date < '{end_time}'"
        f"and ts_code = '{ts_code}' order by trade_date asc"
    )
    data = cur.fetchall()
    db.close()

    return list(data)[0][0]