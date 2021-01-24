from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime  
import os.path  
import sys  
import backtrader as bt
import pandas as pd

# better plotting and results analys
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import blackly, Tradimo

MIN_PERIOD = 30
stk_num = 10  # number of stocks needed back testing

# calculate bar size
def bar_size(datapath, fromdate, todate):
    df = pd.read_csv(datapath)
    return len(df[(df['trade_date'] >= int(fromdate.strftime('%Y%m%d'))) 
            & (df['trade_date'] <= int(todate.strftime('%Y%m%d')))])
    
# adding strategy
class SmaCross(bt.Strategy):
    # strategy parameters
    params = dict(
        pfast=5,  # short period duration
        pslow=30,   # long period duration
        poneplot = False,  # if print on one figure
        pstake = 1000 # trading size
    )
    def __init__(self):
        self.inds = dict()
        for i, d in enumerate(self.datas):
            self.inds[d] = dict()
            self.inds[d]['sma1'] = bt.ind.SMA(d.close, period=self.p.pfast)  
            self.inds[d]['sma2'] = bt.ind.SMA(d.close, period=self.p.pslow)  
            self.inds[d]['cross'] = bt.ind.CrossOver(self.inds[d]['sma1'], self.inds[d]['sma2'], plot = False)  # cross signal
            
            #* skip the first stock as the background stock
            if i > 0:
                if self.p.poneplot:
                    d.plotinfo.plotmaster = self.datas[0]
                    
    def next(self):
        for i, d in enumerate(self.datas):
            dt, dn = self.datetime.date(), d._name           # assign datatime and stock name
            pos = self.getposition(d).size                   # getting current position
            
            if not pos:                                      
                if self.inds[d]['cross'] > 0:                #* buy signal
                    self.buy(data = d, size = self.p.pstake) 
            elif self.inds[d]['cross'] < 0:                  #* sell signal 
                self.close(data = d)                         
                
cerebro = bt.Cerebro()  

# input stock data
stk_code_file = '/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyData/StockList.csv'
stk_pools = pd.read_csv(stk_code_file)

if stk_num > stk_pools.shape[0]:
    print('number of backtesting stock should not be more than %d' % stk_pools.shape[0])
    exit()
    
#! reading all stock data togather 
for i in range(stk_num):
    stk_code = stk_pools['ts_code'][stk_pools.index[i]]
    
    datapath = '/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyData/' + stk_code + '.csv'
    fromdate=datetime.datetime(2019, 1, 15)
    todate=datetime.datetime(2021, 1, 15)
    
    if MIN_PERIOD > bar_size(datapath, fromdate, todate):
        continue
    
    # read data
    
    data = bt.feeds.GenericCSVData(
        dataname=datapath,
        fromdate=fromdate,
        todate=todate,
        nullvalue=0.0,
        dtformat=('%Y%m%d'),
        datetime=1,
        time=-1,
        high=3,
        low=4,
        open=2,
        close=5,
        volume=6,
        openinterest=-1,
        timeframe=bt.TimeFrame.Days,
    )
    
    # add stock name in cerebro
    cerebro.adddata(data, name = stk_code)
    

cerebro.broker.setcash(100000.0)

cerebro.addsizer(bt.sizers.FixedSize, stake = 1000)

cerebro.broker.setcommission(commission=0.0002)
cerebro.addstrategy(SmaCross, poneplot = False)  
cerebro.run()  

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot(style = "candlestick")  
#plot
b = Bokeh(style='bar', plot_mode='single')
cerebro.plot(b)