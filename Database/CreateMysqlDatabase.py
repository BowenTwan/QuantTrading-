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
try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@')
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
        sql0 = f'USE AStockMarket'
        mycursor.execute(sql0)

# Create stock list table 
# set charactor as utf8 so that MySql can read Chinese
try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@')
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
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
            is_hs VARCHAR(50) \
            )'
        
        mycursor.execute(sql1)

# Create Stock daily price table
try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@') 
    if conn.is_connected():
        mycursor = conn.cursor(buffered=True)
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




