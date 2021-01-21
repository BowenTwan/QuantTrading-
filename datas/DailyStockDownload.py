import tushare as ts
from tushare import stock
import pandas as pd
import datetime
import sys
import os

# set up token
pro = ts.pro_api('a0f192a7b75e15dd2d8c16f0a300a6e2b055f55d1589cfef6eb2fa01')

# download all stock daily data 
# save data in csv file for each stock

# downloading data up to today
today = datetime.datetime.now().strftime('%Y%m%d')

# prepare file saving path
father_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
save_path = os.path.join(father_dir, 'AstockDailyData/')

# loading all the stock listed on both shanghai and shenzhen market
stock_list = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,list_date')
# save stock list
stock_list.to_csv(save_path+'StockList.csv')
print(f'stock list downloaded')

# loading stock data 
print(f'starting to dowmload daily data up to {today}')
i = 0

col = ['ts_code','trade_date','open','high','low','close','vol','amount']

for stock_code in stock_list['ts_code']:
    try: 
        stock_data = pro.daily(ts_code=stock_code, start_date='20190101', end_date=today)
        file_name = f'{save_path}{stock_code}.csv'
        stock_price_data = stock_data[col].copy()
        stock_price_data.sort_values(by= 'trade_date', ascending = True).to_csv(file_name, index=False)
        i = i + 1
        
    except:
         print(f'{stock_code} downlaoding data failed')
        
print(f'downloading complete, {i} stocks dowlanded')

