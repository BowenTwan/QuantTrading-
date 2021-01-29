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
    conn = mysql.connect(host = 'localhost', user = 'root', passwd = '201202@', database = 'AStockMarket')
    if conn.is_connected():
        print('Database AStockMarket is connected!')
        mycursor = conn.cursor(buffered=True)
        # get stock code from database
        
        #check the date when database is updated
        mycursor.execute(f'SELECT trade_date FROM Daily ORDER BY trade_date DESC LIMIT 1')
        query_result = mycursor.fetchone()
        last_updated_date = query_result[0]
        
        # refer the date from mysql to python format
        fromdate = datetime.datetime.strptime(query_result[0],'%Y%m%d') + datetime.timedelta(days=1)
        fromdate = datetime.datetime.strftime(fromdate,'%Y%m%d')
        
        # if date update to date, no need to update 
        # updating under other situations 
        if fromdate > today:
            print(f'database up to date!')
        
        else:
            # Retrive today's daily data from Tusahre from last updating date
            df = pro.daily(trade_date=today)
            print(f'Original daily data from {fromdate} to {today} downlaoded from Tushare!')

            value = df.values.tolist()
            mycursor.executemany(sql, value)
            print(f'{fromdate} to {today} daily record inserted')

            conn.commit()
            print(f'{fromdate} to {today} daily records are uploaded to MySql  successfully, total {len(df)} records are inserted \n')
        
        
except Error as e:
    print('Error while connecting to MySql', e)