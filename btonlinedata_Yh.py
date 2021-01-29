'''
Data Source: Yahoo Online
Num of back testing stock: one 
'''

from Strategies.MA20crossover import TestStrategy
import datetime

import backtrader as bt
import pandas as pd
import quantstats
from backtrader.dataseries import TimeFrame

# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Set data parameters and add to Cerebro
today = datetime.datetime.today()
data = bt.feeds.YahooFinanceData(
    dataname='AAPL',
    fromdate=datetime.datetime(2019, 1, 1),
    todate=today
# settings for out-of-sample data
# fromdate=datetime.datetime(2018, 1, 1),
# todate=datetime.datetime(2019, 12, 25))
)

cerebro.adddata(data)


# Add strategy to Cerebro
cerebro.addstrategy(TestStrategy)

# Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=100)

if __name__ == '__main__':
    # Run Cerebro Engine

    # import analyzer 
    # cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')

    # get the banlance of broker account
    start_portfolio_value = cerebro.broker.getvalue()

    # set the commission
    cerebro.broker.setcommission(commission=0.01)

    cerebro.run()
    #results = cerebro.run()
    #strat = results[0]


    # get the final banlance
    end_portfolio_value = cerebro.broker.getvalue()
    # calculate the profot and loss
    pnl = end_portfolio_value - start_portfolio_value
    print(today)
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')
    
    # record performance and save as log file
    # portfolio_stats = strat.analyzers.getbyname('PyFolio')
    # returns, positions, transactions, gross_lev = portfolio_stats.get_pf_items()
    # returns.index = returns.index.tz_convert(None)
    # quantstats.reports.html(returns, output='stats.html', title='BTC Sentiment')
    # cerebro.addwriter(bt.WriterFile, csv=True, out='log.csv')

    # cerebro.plot()
