from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
from Strategies.MA20crossover import TestStrategy

# Import the backtrader platform
import backtrader as bt


if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    #Add a strategy
    strats = cerebro.optstrategy(
        TestStrategy,
        maperiod=range(10, 31)
        )

    # cerebro.addstrategy(TestStrategy)

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'datas/AAPL01132020_01082021.csv')

    # Create a Data Feed for YahooFinance cvs
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2020, 1, 13),
        # Do not pass values before this date
        todate=datetime.datetime(2021, 1, 1),
        # Do not pass values after this date
        reverse=False
        )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(10000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission
    cerebro.broker.setcommission(commission=0.01)

    # Run over everything
    cerebro.run()

    #plot
    cerebro.plot()