from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
from Strategies.Harami import harami

# Import the backtrader platform
import backtrader as bt


if __name__ == '__main__':
    
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    #* Add a strategy
    # strats = cerebro.optstrategy(
    #     TestStrategy,
    #     maperiod=range(10, 31)
    #     )

    cerebro.addstrategy(harami)

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'datas/data_clear.csv')

    # Create a Data Feed for general cvs
    data = bt.feeds.GenericCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2018, 7, 7),
        todate=datetime.datetime(2021,1,1),
        nullvalue=0.0,
        dtformat=('%Y-%m-%d'),
        datetime=0,
        time=-1,
        high=2,
        low=3,
        open=1,
        close=4,
        volume=6,
        openinterest=-1,
        timeframe=bt.TimeFrame.Days,
        compression=1
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
    print(f'Starting Portfolio Value: , {principle:.2f}')

    # Run over everything
    cerebro.run()
    
    banlance = cerebro.broker.getvalue()
    print(f'Ending Portfolio Value: {banlance:.2f}') 
    pnl = banlance - principle
    RR = pnl/principle
    print(f'Profit/Loss: {pnl:.2f}')
    print(f'Return Rate: {RR*100:.2f}%')
    
    #plot
    cerebro.plot()