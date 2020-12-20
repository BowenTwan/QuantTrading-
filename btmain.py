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

# data2 = bt.feeds.GenericCSVData(
#     dataname='multiTimeline.csv',
#     fromdate=datetime.datetime(2017, 1, 1),
#     todate=datetime.datetime(2020, 12, 19),
#     nullvalue=0.0,
#     dtformat=('%Y-%m-%d'),
#     datetime=0,
#     time=-1,
#     high=-1,
#     low=-1,
#     open=-1,
#     close=1,
#     volume=-1,
#     openinterest=-1,
#     timeframe=bt.TimeFrame.Days)

# cerebro.adddata(data2)

# Add strategy to Cerebro
cerebro.addstrategy(MAcrossover)

# Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

if __name__ == '__main__':
    # Run Cerebro Engine
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')

    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run()
    results = cerebro.run()
    strat = results[0]

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')
    
    portfolio_stats = strat.analyzers.getbyname('PyFolio')
    returns, positions, transactions, gross_lev = portfolio_stats.get_pf_items()
    returns.index = returns.index.tz_convert(None)
    quantstats.reports.html(returns, output='stats.html', title='BTC Sentiment')
    cerebro.addwriter(bt.WriterFile, csv=True, out='log.csv')

#cerebro.plot()
