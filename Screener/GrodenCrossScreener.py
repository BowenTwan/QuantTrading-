#* Use golden cross to select stock pool
import pandas as pd
import datetime

def golden_cross(df,fast, slow):
    """
    if the golden corss happens in the last tow day of back testing

    Args:
        df ([type]): data source
        
    """
    # check if the stock has enough trading bar to calculates indicator
    if df.shape[0] < slow:
        return False
    
    # name the indicators
    fast_indicator = f'ma{fast}'
    slow_indicator = f'ma{slow}'
    
    # ruler to decide if the golde cross happening 
    return df[fast_indicator][df.index[0]] > df[slow_indicator][df.index[0]] \
       and df[fast_indicator][df.index[1]] < df[slow_indicator][df.index[1]]
       
# import stock data 
stock_code_file = '/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyData/StockList.csv'
stock = pd.read_csv(stock_code_file)
out_df = pd.DataFrame(columns = ['code'], dtype = str)

# run through all stock data
for stock_code in stock['ts_code']:
    try:
        data_file = f'/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyExData/{stock_code}.csv'
        df = pd.read_csv(data_file)
        df = df.sort_index(ascending = False)
    
        if golden_cross(df,5,20):
            out_df = out_df.append({'code': stock_code}, ignore_index = True)
            print(f'{stock_code} has happened golden cross')
    except:
        pass

# export stock pool
now = datetime.datetime.now()   
out_df.to_csv(f'/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/StockPool/stockpool_{now}.csv')