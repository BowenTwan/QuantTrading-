from os import close
import mysql.connector as mysql
from mysql.connector import charsets
from mysql.connector.errors import Error
import pandas as pd
import tushare as ts
import datetime


# Insert stock list into StockList Table 
#* load data from stocklist csv
today = datetime.datetime.now().strftime('%Y%m%d')
pro = ts.pro_api('a0f192a7b75e15dd2d8c16f0a300a6e2b055f55d1589cfef6eb2fa01')

# Retrive today's daily data from Tusahre
# df = pro.daily(trade_date=today)
# print('Original {today} daily data downlaoded from Tushare!')

try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@')
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
        mycursor.execute('USE AStockMarket')
        print('Database AStockMarket is connected!')
        
        # get stock code from database
        sql = "INSERT INTO Daily VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute('select ts_code from StockList')
        query_result = mycursor.fetchall()
        for i in range(len(query_result)):
            stock_code = [iterm for iterm in query_result[i]][0]
            pro = ts.pro_api('a0f192a7b75e15dd2d8c16f0a300a6e2b055f55d1589cfef6eb2fa01')
            df = pro.daily(ts_code=stock_code, start_date='20080101', end_date=today)
            print(f'downloaded {stock_code} data from 20080101 to {today} from Tusahre')

            value = df.values.tolist()
            mycursor.executemany(sql, value)
            print(f'{stock_code} Record inserted')

            conn.commit()
            print(f'{stock_code} uploads to MySql  successfully, total {len(df)} records are inserted \n')
        
        
except Error as e:
    print('Error while connecting to MySql', e)