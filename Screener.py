import datetime
import backtrader as bt
from strategies import *

class Screener_SMA(bt.Analyzer):
    params = (('period',20), ('devfactor',2),)

    def start(self):
        self.bband = {data: bt.indicators.BollingerBands(data,
                period=self.params.period, devfactor=self.params.devfactor)
                for data in self.datas}

    def stop(self):
        self.rets['over'] = list()
        self.rets['under'] = list()

        for data, band in self.bband.items():
            node = data._name, data.close[0], round(band.lines.bot[0], 2)
            if data > band.lines.bot:
                self.rets['over'].append(node)
            else:
                self.rets['under'].append(node)


#Instantiate Cerebro engine
cerebro = bt.Cerebro()

#Add data to Cerebro
instruments = ['TSLA', 'AAPL', 'GE', 'GRPN']
for ticker in instruments:
    data = bt.feeds.YahooFinanceData(
        dataname=ticker,
        fromdate=datetime.datetime(2020, 1, 1),
        todate=datetime.datetime(2020, 10, 30))
    cerebro.adddata(data) 

#Add analyzer for screener
cerebro.addanalyzer(Screener_SMA)

if __name__ == '__main__':
    #Run Cerebro Engine
    cerebro.run(runonce=False, stdstats=False, writer=True)