import backtrader as bt
import datetime


class KDJ(bt.Strategy):
    #* parameters 
    params = (
        ('phigh',9),('plow',9),('pK',3),('pD',3)
    )
    
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()},{txt}')
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        
        self.order = None
        self.buyprice = None
        self.buycomm = None
        
        # the highest price in N bar
        self.high_price = bt.indicators.Highest(self.data.high, period =self.params.phigh )
        # the lowest price in N bar
        self.low_price = bt.indicators.Lowest(self.data.low, period = self.params.plow)
        # calculate rsv
        self.rsv = 100* bt.DivByZero(
            self.data_close - self.low_price, self.high_price - self.low_price, zero= None
            )
        
        # calculate K which is in less cicyle than N bar
        self.K = bt.indicators.EMA(self.rsv, period = self.params.pK)
        # calculate D 
        self.D = bt.indicators.EMA(self.K, period = self.params.pD)
        #calculate J = 3K- 2D
        self.J = 3*self.K - 2*self.D
        
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

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
                self.bar_executed_close = self.dataclose[0]
            else:
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
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
        self.log(f'Close Price: {self.dataclose[0]:.2f}')
        
        if self.order:
            return
        
        condition1 = self.J[-1] - self.D[-1]
        condition2 = self.J[0] - self.D[0]
        if not self.position:
            if condition1 < 0 and condition2 > 0: 
                self.log(f'Buy Created {self.dataclose[0]:.2f}')
                self.order = self.buy()
                
        else:
            if condition1 > 0 and condition2 < 0: 
                self.log(f'Sell Created {self.dataclose[0]:.2f}')
                self.order = self.sell()
             
