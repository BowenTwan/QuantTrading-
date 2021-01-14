from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])


# Import the backtrader platform
import backtrader as bt
from backtrader import plot

# strategy1_MAcrossover
class MAcrossover(bt.Strategy): 
    # Moving average parameters
    params = (('pfast',5),('pslow',20),)

    def __init__(self):
        # create a list to store the log data 
        self.log_pnl = []
        self.dataclose = self.datas[0].close
        
		# Order variable will contain ongoing order details/status
        self.order = None

        # Instantiate moving averages
        self.slow_sma = bt.indicators.MovingAverageSimple(self.datas[0], 
                        period=self.params.pslow)
        self.fast_sma = bt.indicators.MovingAverageSimple(self.datas[0], 
                        period=self.params.pfast)

        self.crossover = bt.indicators.CrossOver(self.slow_sma, self.fast_sma)

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}') # Comment this line when running optimization
        self.log_pnl.append(f'{dt.isoformat()} {txt}')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
		    # An active Buy/Sell order has been submitted/accepted - Nothing to do
             return
            # Check if an order has been completed
            # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('Buy Executed, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm)
                         )
            else:
                self.log('Sell Executed, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
                
            self.bar_executed = len(self)
            
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Reset orders
        self.order = None
        
    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log(f'Operation Profit, Gross {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')


    def next(self):
        
        #* logging the daily close price 
        # self.log(f'Close price {self.dataclose[0]:.2f}')
    	# Check for open orders
        if self.order:
            return

	# Check if we are in the market
        if not self.position:
            
            # We are not in the market, look for a signal to OPEN trades
                
            #If the 20 SMA is above the 50 SMA

            #if self.crossover > 0: # Fast ma crosses above slow ma
             #   pass # Signal for buy order
             #   self.log(f'BUY CREATE {self.dataclose[0]:2f}')
             #       # Keep track of the created order to avoid a 2nd order
              #  self.order = self.buy()                   
            #elif self.crossover < 0: # Fast ma crosses below slow ma
             #   pass # Signal for sell order
             #   self.log(f'SELL CREATE {self.dataclose[0]:2f}')
                # Keep track of the created order to avoid a 2nd order
              #  self.order = self.sell()

             if self.fast_sma[0] > self.slow_sma[0] and self.fast_sma[-1] < self.slow_sma[-1]:
                 self.log(f'Buy Created {self.dataclose[0]:2f}')
                 # Keep track of the created order to avoid a 2nd order
                 self.order = self.buy()
             #Otherwise if the 20 SMA is below the 50 SMA   
             elif self.fast_sma[0] < self.slow_sma[0] and self.fast_sma[-1] > self.slow_sma[-1]:
                 self.log(f'Sell Created {self.dataclose[0]:2f}')
                 # Keep track of the created order to avoid a 2nd order
                 self.order = self.sell()
        else:
            # We are already in the market, look for a signal to CLOSE trades
            if len(self) >= (self.bar_executed + 5):
                self.log(f'Close Created {self.dataclose[0]:2f}')
                self.order = self.close()

    #def stop(self):
        #self.log('(fSMA Period %2d, sSMA Period %2d) Ending Value %.2f' %
                 #(self.params.pfast, self.params.pslow, self.broker.getvalue()), doprint=True)
    def stop(self):
        with open('custom_log.csv', 'w') as e:
            for line in self.log_pnl:
                e.write(line + '\n')