import datetime
import backtrader as bt
from backtrader.dataseries import TimeFrame
from strategies import *
import pandas as pd
import quantstats


# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Set data parameters and add to Cerebro
data1 = bt.feeds.YahooFinanceData(
    dataname='TSLA',
    fromdate=datetime.datetime(2017, 1, 1),
    todate=datetime.datetime(2020, 12, 19)
)
# settings for out-of-sample data
# fromdate=datetime.datetime(2018, 1, 1),
# todate=datetime.datetime(2019, 12, 25))

cerebro.adddata(data1)


# Add strategy to Cerebro
cerebro.addstrategy(MAcrossover)

# Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

if __name__ == '__main__':
    # Run Cerebro Engine

    # import analyzer 
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')

    # get the banlance of broker account
    start_portfolio_value = cerebro.broker.getvalue()

    # set the commission
    cerebro.broker.setcommission(commission=0.0)

    cerebro.run(maxcpus=-1)
    results = cerebro.run()
    strat = results[0]


    # get the final banlance
    end_portfolio_value = cerebro.broker.getvalue()
    # calculate the profot and loss
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')
    
    # record performance and save as log file
    portfolio_stats = strat.analyzers.getbyname('PyFolio')
    returns, positions, transactions, gross_lev = portfolio_stats.get_pf_items()
    returns.index = returns.index.tz_convert(None)
    quantstats.reports.html(returns, output='stats.html', title='BTC Sentiment')
    cerebro.addwriter(bt.WriterFile, csv=True, out='log.csv')

#cerebro.plot()
