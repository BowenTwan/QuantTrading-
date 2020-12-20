from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])


# Import the backtrader platform
import backtrader as bt
from backtrader import plot

class MAcrossover(bt.Strategy): 
    # Moving average parameters
    params = (('pfast',20),('pslow',50),)

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
                self.log(f'BUY EXECUTED, {order.executed.price:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED, {order.executed.price:.2f}')
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Reset orders
        self.order = None

    def next(self):
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
                 self.log(f'BUY CREATE {self.dataclose[0]:2f}')
                 # Keep track of the created order to avoid a 2nd order
                 self.order = self.buy()
             #Otherwise if the 20 SMA is below the 50 SMA   
             elif self.fast_sma[0] < self.slow_sma[0] and self.fast_sma[-1] > self.slow_sma[-1]:
                 self.log(f'SELL CREATE {self.dataclose[0]:2f}')
                 # Keep track of the created order to avoid a 2nd order
                 self.order = self.sell()
        else:
            # We are already in the market, look for a signal to CLOSE trades
            if len(self) >= (self.bar_executed + 5):
                self.log(f'CLOSE CREATE {self.dataclose[0]:2f}')
                self.order = self.close()

    #def stop(self):
        #self.log('(fSMA Period %2d, sSMA Period %2d) Ending Value %.2f' %
                 #(self.params.pfast, self.params.pslow, self.broker.getvalue()), doprint=True)
    def stop(self):
        with open('custom_log.csv', 'w') as e:
            for line in self.log_file:
                e.write(line + '\n')





class TestStrategy(bt.Strategy):
    params = (
        ('maperiod', 15),
        ('printlog', False),
    )

    def log(self, txt, dt=None, doprint=False):
        ''' Logging function fot this strategy'''
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Add a MovingAverageSimple indicator
        self.sma = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=self.params.maperiod)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] > self.sma[0]:

                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()

        else:

            if self.dataclose[0] < self.sma[0]:
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()

    def stop(self):
        self.log('(MA Period %2d) Ending Value %.2f' %
                 (self.params.maperiod, self.broker.getvalue()), doprint=True)

class AverageTrueRange(bt.Strategy):
    
	def log(self, txt, dt=None):
		dt = dt or self.datas[0].datetime.date(0)
		print(f'{dt.isoformat()} {txt}') #Print date and close
		
	def __init__(self):
		self.dataclose = self.datas[0].close
		self.datahigh = self.datas[0].high
		self.datalow = self.datas[0].low
		
	def next(self):
		range_total = 0
		for i in range(-13, 1):
			true_range = self.datahigh[i] - self.datalow[i]
			range_total += true_range
		ATR = range_total / 14

		self.log(f'Close: {self.dataclose[0]:.2f}, ATR: {ATR:.4f}')

#simple moving average
class SimpleMA(bt.Strategy):
    def __init__(self):
        self.sma1 = bt.indicators.SimpleMovingAverage(self.data, period=1, 
                plotname="1 SMA")
        self.sma2 = bt.indicators.SimpleMovingAverage(self.data, period=144,
                plotname="20 SMA")



class BtcSentiment(bt.Strategy):
    params = (('period', 10), ('devfactor', 1),)

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')

    def __init__(self):
        self.btc_price = self.datas[0].close
        self.google_sentiment = self.datas[1].close
        self.bbands = bt.indicators.BollingerBands(self.google_sentiment,
                period=self.params.period, devfactor=self.params.devfactor)

        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Existing order - Nothing to do
            return
        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash


        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, {order.executed.price:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED, {order.executed.price:.2f}')
                self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, 
                              order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Reset orders
        self.order = None
    def next(self):
        # Check for open orders
        if self.order:
            return

		#Long signal
        if self.google_sentiment > self.bbands.lines.top[0]:
			# Check if we are in the market
            if not self.position:
                self.log(f'Google Sentiment Value: {self.google_sentiment[0]:.2f}')
                self.log(f'Top band: {self.bbands.lines.top[0]:.2f}')
				# We are not in the market, we will open a trade
                self.log(f'***BUY CREATE {self.btc_price[0]:.2f}')
				# Keep track of the created order to avoid a 2nd order
                self.order = self.buy()       

		#Short signal
        elif self.google_sentiment < self.bbands.lines.bot[0]:
			# Check if we are in the market
            if not self.position:
                self.log(f'Google Sentiment Value: {self.google_sentiment[0]:.2f}')
                self.log(f'Bottom band: {self.bbands.lines.bot[0]:.2f}')
				# We are not in the market, we will open a trade
                self.log(f'***SELL CREATE {self.btc_price[0]:.2f}')
				# Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
		
		#Neutral signal - close any open trades     
        else:
            if self.position:
				# We are in the market, we will close the existing trade
                self.log(f'Google Sentiment Value: {self.google_sentiment[0]:.2f}')
                self.log(f'Bottom band: {self.bbands.lines.bot[0]:.2f}')
                self.log(f'Top band: {self.bbands.lines.top[0]:.2f}')
                self.log(f'CLOSE CREATE {self.btc_price[0]:.2f}')
                self.order = self.close()