import datetime
import backtrader as bt
from strategies import *

cerebro = bt.Cerebro(optreturn=False)

#Set data parameters and add to Cerebro
data = bt.feeds.YahooFinanceData(
    dataname='TSLA',
    fromdate=datetime.datetime(2016, 1, 1),
    todate=datetime.datetime(2017, 12, 25))
    #settings for out-of-sample data
    #fromdate=datetime.datetime(2018, 1, 1),
    #todate=datetime.datetime(2019, 12, 25))

cerebro.adddata(data)

#Add strategy to Cerebro
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe_ratio')
cerebro.optstrategy(TestStrategy, maperiod=range(5, 30))  

#Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

if __name__ == '__main__':
    optimized_runs = cerebro.run()

    final_results_list = []
    for run in optimized_runs:
        for strategy in run:
            PnL = round(strategy.broker.get_value() - 10000,2)
            sharpe = strategy.analyzers.sharpe_ratio.get_analysis()
            final_results_list.append([strategy.params.maperiod, 
                PnL, sharpe['sharperatio']])

    sort_by_sharpe = sorted(final_results_list, key=lambda x: x[1], 
                             reverse=True)
    for line in sort_by_sharpe[:5]:
        print(line)