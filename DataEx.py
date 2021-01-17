from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import os.path  # manage the file path
import sys
from pandas_ta.volatility.true_range import true_range  # fine the script name 
import pandas as pd
import btalib as btb

# create new directory
script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
ExData_path = os.path.join(script_path, 'datas/AstockDailyExData/')
OriginalData_path = os.path.join(script_path, 'datas/AstockDailyData/')

# read stock code
stk_pools = pd.read_csv(f'{OriginalData_path}StockList.csv')

# add calculated indicator into original file
for stk_code in stk_pools['ts_code']:

# short cut for checking the code     
# for stk_code in ('000001.sz', '000002.sz'):
    try:
    # input original daily stock price data 
        input_file = OriginalData_path + stk_code + '.csv'
        df = pd.read_csv(input_file, index_col = 0)
        df = df.sort_index(ascending = True)
        
        # MA
        ma_list = [5, 10, 20, 30, 60]
        for i in ma_list:
            df[f'ma{i}'] = pd.Series(btb.sma(df, period = i), index = df.index)
        
        # # vol_MA
        # vol_ma_list = [5, 10, 20, 30, 60, 120, 240]
        # for i in vol_ma_list:
        #     df = ta.vol_MA_n(df, i)
        
        #BBANDS
        df['bbands_up'] = btb.bbands(df, period = 20)['top']
        
        # #MACD
        # df = ta.MACD020(df, 12, 26)
        # #KDJ
        # df = ta.KDJ(df, 9, 3)
        # #RSI
        # df = ta.RSI(df, 14)
        
        # save the new file
        output_file = ExData_path + stk_code +'.csv'
        df.to_csv(output_file)
        
        # for checking the code 
        # print(df.tail(5))
        
    except:
        print(f'{stk_code} can not calculate indicators')
