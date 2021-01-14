import backtrader as bt
from backtrader import cerebro
import numpy as np

class harami(bt.Strategy):
    """
    this is strategy using candel chart identification to locate the buy signal
    harami is where the previouse day candel chart surrounds the next day candel chart
    """
    
    def log(self,txt, dt=None):
        """
        logging the precess
        """
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')
        
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open
        self.datalow = self.datas[0].low
        self.datahigh = self.datas[0].high
        
        self.order = None
        self.profits = []
        
        
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
                
                #! record the buy price and commission
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
                self.bar_executed_close = self.dataclose[0]
            else:
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
                
                #! calculate profit rate
                profit_rate = float(order.executed.price - self.buyprice)/float(self.buyprice)
                # save profit_rate 
                self.profits.append(profit_rate)
                
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
        
    def next(self):
        #self.log(f'Close Price: {self.dataclose[0]:.2f}')
        
        if self.order:
            return
        
        if not self.position:
            if self.dataclose[-1] < self.dataopen[-1]:
                harami = (
                    self.datahigh[0] < self.dataopen[-1]
                    and self.datalow[0] > self.dataclose[-1]
                )
                
            else: 
                harami = (
                    self.datahigh[0] < self.dataclose[-1]
                    and self.datalow[0] > self.dataopen[-1]                   
                )
            
            if harami:
                self.log(f'Bull Create {self.dataclose[0]:.2f}')
                self.order = self.buy()
            
        else:
            #condition = (self.dataclose[0] - self.bar_executed_close) / self.dataclose[0]
            condition = self.bar_executed
            #if condition >0.1 or condition< 0.1:
            if condition > 5:
                self.log(f'Sell Created {self.dataclose[0]:.2f}')
                self.order = self.sell()
                
    # def stop(self):
    #     print(self.profits)
    #     print(f'mean profit rate: {np.mean(self.profits):.2f}')