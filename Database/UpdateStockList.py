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


try:
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@', database = 'AStockMarket')
    if conn.is_connected():
        print('Database AStockMarket is connected!')
        mycursor = conn.cursor(buffered=True)
        
        #check the date when database is updated
        mycursor.execute(f'SELECT list_date FROM StockList ORDER BY list_date DESC LIMIT 1')
        query_result = mycursor.fetchone()
        last_updated_date = query_result[0]
        
        # refer the date from mysql to python format
        fromdate = datetime.datetime.strptime(query_result[0],'%Y%m%d') + datetime.timedelta(days=1)
        fromdate = datetime.datetime.strftime(fromdate,'%Y%m%d')
        
        # downloading latest version of stock list 
        stock_list = pro.stock_basic(exchange='', list_status='',\
            fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
        print('Original data downlaoded from Tushare!')
        
        
        if fromdate > today:
            print(f'Stock List is up to date')
            
        else:
            # # print out new IPO after some day
            stock_list_new = stock_list[stock_list['list_date'] >= fromdate] 
            print(stock_list_new)

            # insert data 
            # only insert NEW IPO stock
            for i,row in stock_list_new.iterrows():
                try: 
                    sql = "INSERT INTO StockList VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(sql, tuple(row))
                    print("New stock list record inserted")
                    
                    # the connection is not autocommitted by default, so we must commit to save our changes
                    conn.commit()
                    
                except:
                    pass
            
except Error as e:
    print('Error while connecting to MySql', e)