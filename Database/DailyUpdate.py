'''
This script is used to update daily A stock market data,
needed to be run after every trading day.
'''

import mysql.connector as mysql
from mysql.connector.errors import Error
import tushare as ts
import datetime


# Insert stock list into StockList Table 
#* load data from stocklist csv
today = datetime.datetime.now().strftime('%Y%m%d')
pro = ts.pro_api('a0f192a7b75e15dd2d8c16f0a300a6e2b055f55d1589cfef6eb2fa01')
sql = "INSERT INTO Daily VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


try:
    # connecting to MySql
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@')
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
        mycursor.execute('USE AStockMarket')
        print('Database AStockMarket is connected!')
        
        # get stock code from database
        
        # Retrive today's daily data from Tusahre
        df = pro.daily(trade_date=today)
        print('Original {today} daily data downlaoded from Tushare!')

        value = df.values.tolist()
        mycursor.executemany(sql, value)
        print(f'{today} daily record inserted')

        conn.commit()
        print(f'{today} daily records are uploaded to MySql  successfully, total {len(df)} records are inserted \n')
        
        
except Error as e:
    print('Error while connecting to MySql', e)