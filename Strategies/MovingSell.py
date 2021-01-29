'''
Strategy
Buy Signal: godlen cross: sma5 up cross sma60
Sell Signal: sell stock when price is either lower than close at open day minus 5% 
                or lower than higher close price after open day minus 5%

'''

import backtrader as bt
import datetime

class MovingSell(bt.Strategy):
    params = dict(
        pfast = 5,
        pslow = 60,
        trailpercent = 0.05,
        buy_valid_date = 5,
        buy_limit_percent = 0.01,
        trailamount = 0.0
    )
    # log function 
    def log(self,txt, dt=None):
        """
        logging the precess
        """
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')
        
    def __init__(self):
        
        sma5 = bt.ind.SMA(period = self.p.pfast)
        sma60 = bt.ind.SMA(period = self.p.pslow) 
        self.buy_condition = bt.ind.CrossUp(sma5, sma60)
        self.dataclose = self.datas[0].close
        self.order = None
        
    def notify_order(self, order):
        if order.status in [order.Completed]:
            print('Completed order: {}: Order ref: {} / Type {} / Status {} '.format(
            self.data.datetime.date(0),
            order.ref, 'Buy' * order.isbuy() or 'Sell',
            order.getstatusname()))
            self.order = None
        if order.status in [order.Expired]:
            self.order = None
            self.log(f"Order ref: {order.ref} / Type {'Buy' * order.isbuy() or 'Sell'} / Status {order.getstatusname()}")
    
        
    def next(self):
        # no position in market
        if not self.position:
            # no order submitted
            if None == self.order:
                if self.buy_condition:
                    # set up buy order validation period 
                    # if order is not executed in validtion, cancel buy order 
                    valid = self.data.datetime.date(0)
                    if self.p.buy_valid_date:
                        valid = valid + datetime.timedelta(days = self.p.buy_valid_date)
                        # calculate buying price 
                        price = self.dataclose * (1 - self.p.buy_limit_percent)
                        self.order = self.buy(exectype = bt.Order.Limit, price = price, valid=valid)
                        self.log(f'Buy order created, close: {self.dataclose}, limit price:{price}, valid: {valid}')
                        print('*' * 10)
                        
        elif self.order is None:
            # submit stoptail order
            self.order = self.sell(exectype = bt.Order.StopTrail,
                                   trailamount = self.p.trailamount,
                                   trailpercent = self.p.trailpercent)
            
            if self.p.trailamount:
                tcheck = self.dataclose - self.p.trailamount
            else:
                tcheck = self.dataclose * (1 - self.p.trailpercent)
            self.log(f'Sell stoptrail order created, close: {self.dataclose}, limit price {self.order.created.price}, check price {tcheck}')
            print('*' * 10)
            
        else:
            if self.p.trailamount:
                tcheck = self.dataclose - self.p.trailamount
            else:
                tcheck = self.dataclose * (1.0 - self.p.trailpercent)
            self.log(f'update limit price, close: {self.dataclose}, limit price: {self.order.created.price} / check price {tcheck}')