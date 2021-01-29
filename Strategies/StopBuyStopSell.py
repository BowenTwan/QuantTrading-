'''
strategy
buy signal: when there is 4 days down in a row for one stock 
sell signal: 1) when profit is reaching 10% or 2) loss 5% of the principle
'''

import backtrader as bt
import datetime

class StopBuyStopSell(bt.Strategy):
    # setting up parameters
    params = dict(
        p_downdays = 4,
        limit = 0.0005,
        p_stoploss = 0.05,
        p_limitprofit = 0.1,
        limitdays1 = 3,
        limitdays23 = 1000,
        
    )
    
    # log function 
    def log(self,txt, dt=None):
        """
        logging the precess
        """
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')
        
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.orefs = list()
    
    def notify_order(self, order):
        print(f"{self.data.datetime.date(0)} :order ref :{order.ref} / type {'Buy' * order.isbuy() or 'Sell'} / status {order.getstatusname()}")
        
        if order.status == order.Completed:
            self.holdstart = len(self)

        if not order.alive() and order.ref in self.orefs:
            self.orefs.remove(order.ref)
            
        
    def next(self): 
        if self.orefs: # orefs, order reference, is uesd to store unfinish orders 
            return False
        
        if not self.position:
            
            # list used to store the last few days' close 
            lastclosed = list()
            for i in range(self.p.p_downdays +1):
                lastclosed.append(self.dataclose[-1])
                
            if lastclosed == sorted(lastclosed): # decide if price goes down in 4 days 
                close = self.dataclose[0]
                # calculate buy price p1, stop lossprice p2, limite price p3
                p1 = close * (1-self.p.limit)
                p2 = p1  - self.p.p_stoploss * close
                p3 = p1 - self.p.p_limitprofit * close
                
                # set validation period for bucket order
                valid1 = datetime.timedelta(self.p.limitdays1)
                valid23 = datetime.timedelta(self.p.limitdays23)
                
                # using bucket order
                bucket_order = self.buy_bracket(
                    price= p1, valid= valid1,
                    stopprice= p2, stopargs={'valid': valid23},
                    limitprice= p3, limitargs={'valid': valid23}
                )
                
                #save orders 
                self.orefs = [o.ref for o in bucket_order]