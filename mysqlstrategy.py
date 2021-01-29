'''
Data source: MySql
Num of backtesting stock: one 
'''


from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
from Strategies.MovingSell import MovingSell


# Import the backtrader platform
import backtrader as bt
from backtrader.feeds.mysqlfeed import MySQLData

# better plotting and results analys
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import blackly, Tradimo

if __name__ == '__main__':
    
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    #* Add a strategy
    # strats = cerebro.optstrategy(
    #     TestStrategy,
    #     maperiod=range(10, 31)
    #     )

    cerebro.addstrategy(MovingSell)


    # Create a Data Feed for general cvs
    data = MySQLData(
        fromdate = datetime.datetime(2020, 1, 1),
        todate = datetime.datetime(2021,1,22),
        ts_code = '000001.SZ'
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

    # Set the commission
    cerebro.broker.setcommission(commission=0.0002)
    
    principle = cerebro.broker.getvalue()
    print(f'Starting Portfolio Value: {principle:.2f}')
    
    # add analyser
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DW')

    # Run over everything
    backtest = cerebro.run()
    strat = backtest[0]
    
    banlance = cerebro.broker.getvalue()
    print(f'Ending Portfolio Value: {banlance:.2f}') 
    pnl = banlance - principle
    RR = pnl/principle
    print(f'Profit/Loss: {pnl:.2f}')
    print(f'Return Rate: {RR*100:.2f}%')
    print('Sharpe Ratio:', strat.analyzers.SharpeRatio.get_analysis())
    print('Draw Down:', strat.analyzers.DW.get_analysis())
    
    #plot
    b = Bokeh(style='bar', plot_mode='single')
    cerebro.plot(b)