from os import close
import mysql.connector as mysql
from mysql.connector import charsets
from mysql.connector.errors import Error
import pandas as pd
import tushare as ts
import datetime


# connect to Mysql Sever 
try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@')
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
        print('MySql Database is connected!')
    
except Error as e:
    print('Error while connecting to MySql', e)
    

# Create A stock market Database
#mycursor.execute("DROP DATABASE IF EXISTS test; CREATE DATABASE AStockMarket")

# use database Astockmarket
if conn.is_connected():
    mycursor = conn.cursor(buffered=True)
    sql0 = f'USE AStockMarket'
    mycursor.execute(sql0)

# Create stock list table 
if conn.is_connected():
    sql1 = f'CREATE TABLE IF NOT EXISTS StockList(\
        ts_code VARCHAR(225) PRIMARY KEY, \
        symbol VARCHAR(225), \
        name VARCHAR(225) CHARACTER SET utf8 COLLATE utf8_general_ci, \
        area VARCHAR(225) CHARACTER SET utf8 COLLATE utf8_general_ci, \
        industry VARCHAR(225) CHARACTER SET utf8 COLLATE utf8_general_ci, \
        fullname VARCHAR(225) CHARACTER SET utf8 COLLATE utf8_general_ci, \
        enname VARCHAR(225), \
        market VARCHAR(225) CHARACTER SET utf8 COLLATE utf8_general_ci, \
        exchange VARCHAR(225), \
        curr_type VARCHAR(225), \
        list_status VARCHAR(225), \
        list_date VARCHAR(225), \
        delist_date VARCHAR(225), \
        is_hs VARCHAR(225) \
        )'
    
    mycursor.execute(sql1)

# Create Stock daily price table 
if conn.is_connected():
    sql2 = f'CREATE TABLE IF NOT EXISTS Daily(\
        ts_code VARCHAR (50), \
        trade_date VARCHAR(50), \
        open FLOAT, \
        high FLOAT, \
        low FLOAT, \
        close FLOAT, \
        pre_close FLOAT,\
        changes FLOAT, \
        pct_change FLOAT, \
        vol FLOAT, \
        amount FLOAT, \
        FOREIGN KEY(ts_code) REFERENCES StockList(ts_code) \
        )'

    mycursor.execute(sql2)


# Insert stock list into StockList Table 
# load data from stocklist csv
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

# Insert daily data in to table 

