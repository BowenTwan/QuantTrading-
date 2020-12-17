import backtrader as bt
from datetime import datetime

class PrintClose(bt.Strategy):

    def __init__(self):
        #Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])


#Instantiate Cerebro engine
cerebro = bt.Cerebro()

#Add data feed to Cerebro
data = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2011, 1, 1),
                                  todate=datetime(2012, 12, 31))
cerebro.adddata(data)

## Add your own data, the data is supposed to be under current working foler 
#data = bt.feeds.YahooFinanceCSVData(dataname='TSLA.csv') 
#cerebro.adddata(data) 


#Add strategy to Cerebro
cerebro.addstrategy(PrintClose)

#Run Cerebro Engine
cerebro.run()