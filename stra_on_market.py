"""
1. This script is used to apply strategy on mutiple stock for back testing
2. The backtesting results will be saved 
3. Back testing data is uploaded localy 
"""
    
import datetime
import os
import sys
import backtrader as bt
from Strategies.Harami import harami
import pickle
import matplotlib.pyplot as plt


def run_strategy(stock_file, result):
        """
        run the strategy for mutiple stocks 
        param1: stock_file 
        param2:
        """
        # set up running engine
        cerebro = bt.Cerebro()
        
        # add strategy
        cerebro.addstrategy(harami)
        
        # add data
        data = bt.feeds.GenericCSVData(
            dataname=stock_file,
            fromdate=datetime.datetime(2010, 1, 1),
            todate=datetime.datetime(2020, 4, 25),
            dtformat='%Y%m%d',
            datetime=2,
            open=3,
            high=4,
            low=5,
            close=6,
            volume=10,
            reverse=True
        )
        cerebro.adddata(data)
        
        # order setting: 
        # set principle
        cerebro.broker.setcash(100000)
        # set commission
        cerebro.broker.setcommission(commission = 0.0002)
        # set position number 
        cerebro.addsizer(bt.sizers.FixedSize, stake=100)
        
        cerebro.run()
        
        # calculate return rate
        stock_name = stock_file.split('/')[-1].split('.csv')[0]
        banlance = cerebro.broker.getvalue()
        result[stock_name] = float(banlance - 100000) / 10000
        
# run through all stock file 
file_path = '/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/Astock_Market/'
result = {}

for stock in os.listdir(file_path):
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, file_path+stock)
    print(datapath)
    
    try:
        run_strategy(datapath,result)
    except Exception as e:
        print(e)
        
file = open('./batch_macd_results.txt', 'wb')
pickle.dump(result, file)
file.close()


#* analysis results
file = open('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/VNPY/batch_macd_results.txt', 'rb')
data = pickle.load(file)
file.close()

pos = []
neg = []
ten_pos = []
ten_neg = []

for result in data:
    res = data[result]
    if res > 0:
        pos.append(res)
    else:
        neg.append(res)
        
    if res > 0.1: 
        ten_pos.append(result)
    elif res < -0.1:
        ten_neg.append(result)
        
max_stock = max(data, key=data.get)
print(f'the highest return stock： {max_stock}, reach {data[max_stock]}')
print(f'number of positive return stock: {len(pos)}, number of negtive return stock:{len(neg)}')
print(f'+10%: {len(ten_pos)}, -10%:{len(ten_neg)}')
print(f'return higher than 10%: {ten_pos}')

plt.hist(pos, facecolor='red',edgecolor = 'black', alpha = 0.7)
plt.hist(neg, facecolor='green',edgecolor = 'black', alpha = 0.7)                
plt.show()