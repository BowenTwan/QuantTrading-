import backtrader as bt
from datetime import datetime


class maCross(bt.Strategy):
    '''
    For an official backtrader blog on this topic please take a look at:

    https://www.backtrader.com/blog/posts/2017-04-09-multi-example/multi-example.html

    oneplot = Force all datas to plot on the same master.
    '''
    params = (
    ('sma1', 40),
    ('sma2', 200),
    ('oneplot', True)
    )

    def __init__(self):
        '''
        Create an dictionary of indicators so that we can dynamically add the
        indicators to the strategy using a loop. This mean the strategy will
        work with any numner of data feeds. 
        '''
        self.inds = dict()
        for i, d in enumerate(self.datas):
            self.inds[d] = dict()
            self.inds[d]['sma1'] = bt.indicators.SimpleMovingAverage(
                d.close, period=self.params.sma1)
            self.inds[d]['sma2'] = bt.indicators.SimpleMovingAverage(
                d.close, period=self.params.sma2)
            self.inds[d]['cross'] = bt.indicators.CrossOver(self.inds[d]['sma1'],self.inds[d]['sma2'])

            if i > 0: #Check we are not on the first loop of data feed:
                if self.p.oneplot == True:
                    d.plotinfo.plotmaster = self.datas[0]

    def next(self):
        for i, d in enumerate(self.datas):
            dt, dn = self.datetime.date(), d._name
            pos = self.getposition(d).size
            if not pos:  # no market / no orders
                if self.inds[d]['cross'][0] == 1:
                    self.buy(data=d, size=1000)
                elif self.inds[d]['cross'][0] == -1:
                    self.sell(data=d, size=1000)
            else:
                if self.inds[d]['cross'][0] == 1:
                    self.close(data=d)
                    self.buy(data=d, size=1000)
                elif self.inds[d]['cross'][0] == -1:
                    self.close(data=d)
                    self.sell(data=d, size=1000)

    def notify_trade(self, trade):
        dt = self.data.datetime.date()
        if trade.isclosed:
            print('{} {} Closed: PnL Gross {}, Net {}'.format(
                                                dt,
                                                trade.data._name,
                                                round(trade.pnl,2),
                                                round(trade.pnlcomm,2)))


# class OandaCSVData(bt.feeds.GenericCSVData):
#     params = (
#         ('nullvalue', float('NaN')),
#         #('dtformat', '%Y-%m-%dT%H:%M:%S.%fZ'),
#         ('dtformat', '%Y%m%d'),
#         ('datetime', 0),
#         ('time', -1),
#         ('open', 1),
#         ('high', 2),
#         ('low', 3),
#         ('close', 4),
#         ('volume', 6),
#         ('openinterest', -1),
#     )

class OandaCSVData(bt.feeds.GenericCSVData):
    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%Y%m%d'),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1),
    )
    
#Variable for our starting cash
startcash = 10000

#Create an instance of cerebro
cerebro = bt.Cerebro()

#Add our strategy
cerebro.addstrategy(maCross, oneplot=False)

# create our data list
datalist = [
    ('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/debug/data/000001.SZ.csv', 'CADCHF'), #[0] = Data file, [1] = Data name
    ('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/debug/data/000002.SZ.csv', 'EURUSD'),
    ('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/debug/data/000004.SZ.csv', 'GBPAUD'),
]
# datalist = [
#     ('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/debug/data/CAD_CHF-2005-2017-D1.csv', 'CADCHF'), #[0] = Data file, [1] = Data name
#     ('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/debug/data/EUR_USD-2005-2017-D1.csv', 'EURUSD'),
#     ('/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/debug/data/GBP_AUD-2005-2017-D1.csv', 'GBPAUD'),
# ]
#Loop through the list adding to cerebro.
for i in range(len(datalist)):
    data = OandaCSVData(dataname=datalist[i][0],
                        #fromdate = datetime(2019,1,15),
                        #todate = datetime(2021,1,15),
                        )
    cerebro.adddata(data, name=datalist[i][1])


# Set our desired cash start
cerebro.broker.setcash(startcash)

# Run over everything
cerebro.run()

#Get final portfolio Value
portvalue = cerebro.broker.getvalue()
pnl = portvalue - startcash

#Print out the final result
print('Final Portfolio Value: ${}'.format(portvalue))
print('P/L: ${}'.format(pnl))

#Finally plot the end results
cerebro.plot(style='candlestick')