from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
 
import backtrader as bt

# adding strategy
class SmaCross(bt.Strategy):
    # strategy parameters
    params = dict(
        pfast=5,  # short period duration
        pslow=30,   # long period duration
        poneplot = False,  # if print on one figure
        pstake = 1000 # trading size
    )
    def __init__(self):
        self.inds = dict()
        for i, d in enumerate(self.datas):
            self.inds[d] = dict()
            self.inds[d]['sma1'] = bt.ind.SMA(d.close, period=self.p.pfast)  
            self.inds[d]['sma2'] = bt.ind.SMA(d.close, period=self.p.pslow)  
            self.inds[d]['cross'] = bt.ind.CrossOver(self.inds[d]['sma1'], self.inds[d]['sma2'], plot = False)  # cross signal
            
            #* skip the first stock as the background stock
            if i > 0:
                if self.p.poneplot:
                    d.plotinfo.plotmaster = self.datas[0]
                    
    def next(self):
        for i, d in enumerate(self.datas):
            dt, dn = self.datetime.date(), d._name           # assign datatime and stock name
            pos = self.getposition(d).size                   # getting current position
            
            if not pos:                                      
                if self.inds[d]['cross'] > 0:                #* buy signal
                    self.buy(data = d, size = self.p.pstake) 
            elif self.inds[d]['cross'] < 0:                  #* sell signal 
                self.close(data = d)   