# test test join quant data downloading 
import tushare as ts
pro = ts.pro_api('a0f192a7b75e15dd2d8c16f0a300a6e2b055f55d1589cfef6eb2fa01')
df = pro.daily(ts_code='000002.SZ', start_date='20180701', end_date='20210108')
print(df)
df.to_csv('data.csv')


# test test join quant data downloading 

# import jqdatasdk as jd
# jd.auth('18328314344','314344')
# df = jd.get_price(security = '000001.XSHE',frequency = '1d', panel = True)
# print(df)