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
stock_list = pro.stock_basic(exchange='', list_status='',\
    fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
print('Original data downlaoded from Tushare!')
print(stock_list.head())

try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@')
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
        mycursor.execute('USE AStockMarket')
        print('Database AStockMarket is connected!')
        # insert data 
        for i,row in stock_list.iterrows():
            sql = "INSERT INTO StockList VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql, tuple(row))
            print("Record inserted")
            
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print('Error while connecting to MySql', e)