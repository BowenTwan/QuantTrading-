'''
Data Source: MySql
Num of back testing stock: Mutiple 
Need to Specify stock pools
'''


from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import pandas as pd
from Strategies.SMACross import SmaCross
from Database.DataBaseFunctions import length_calculator_db

# Import the backtrader platform
import backtrader as bt
from backtrader.feeds.mysqlfeed import MySQLData

# better plotting and results analys
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import blackly, Tradimo

#* decide the how many stock needed to back test 
stock_number = 2
#* the minimus bar to calculat necessary indicators 
MIN_PERIOD = 20

#* decide the stock pool 
stock_pool = ['000001.SZ','000002.SZ','000004.SZ']

#* back test period 
fromdate=datetime.datetime(2019, 1, 15)
todate=datetime.datetime(2021, 1, 15)

    
if __name__ == '__main__':

    # number of backtest stock should be more than stock pool stock numbers 
    # otherwise exit this procedu
    if stock_number > len(stock_pool):
        print(f'number of backtesting stock should be more than {len(stock_pool)}')
        exit()
    
    else:
        # Create a cerebro entity
        cerebro = bt.Cerebro()

        #* Add a strategy
        # strats = cerebro.optstrategy(
        #     TestStrategy,
        #     maperiod=range(10, 31)
        #     )
        cerebro.addstrategy(SmaCross)

        # add data from MySql for all stocks in pool
        for i in range(3):
            stock_code = stock_pool[i]
        
            # check if the bar_size is enough to calculate the indicator 
            if MIN_PERIOD > length_calculator_db('Daily',stock_code,fromdate,todate):
                continue
            
            data = MySQLData(
                fromdate = fromdate,
                todate = todate,
                ts_code = stock_code
            )
            # Add the Data Feed to Cerebro
            cerebro.adddata(data, name = stock_code)

        # Set our desired cash start
        cerebro.broker.setcash(100000.0)

        # Add a FixedSize sizer according to the stake
        cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

        # Set the commission
        cerebro.broker.setcommission(commission=0.0002)
        
        # get starting fund 
        principle = cerebro.broker.getvalue()
        print(f'Starting Portfolio Value: {principle:.2f}')
        
        # add analyser
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'SharpeRatio')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DW')

        # Run over everything
        back_test = cerebro.run()
        strat = back_test[0]
        banlance = cerebro.broker.getvalue()
        print(f'Ending Portfolio Value: {banlance:.2f}') 
        pnl = banlance - principle
        RR = pnl/principle
        print(f'Profit/Loss: {pnl:.2f}')
        print(f'Return Rate: {RR*100:.2f}%')
        print('SR:', strat.analyzers.SharpeRatio.get_analysis())
        print('DW:', strat.analyzers.DW.get_analysis())

        #plot
        b = Bokeh(style='bar', plot_mode='single')
        cerebro.plot(b)