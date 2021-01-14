import tushare as ts
import pandas as pd
pro = ts.pro_api('a0f192a7b75e15dd2d8c16f0a300a6e2b055f55d1589cfef6eb2fa01')


astock = pro.query('stock_basic', 
    exchange='', 
    list_status='L', 
    fields='ts_code,symbol,name,fullname,enname,area,industry,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

astock.to_csv('Astock.csv',)