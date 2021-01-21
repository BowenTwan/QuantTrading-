from __future__ import (absolute_import, division, print_function, unicode_literals)
import datetime  # 用于datetime对象操作
import os.path  # 用于管理路径
import sys  # 用于在argvTo[0]中找到脚本名称
import backtrader as bt # 引入backtrader框架
import pandas as pd

MIN_PERIOD = 30
stk_num = 2  # 回测股票数目

# calculate bar size
def bar_size(datapath, fromdate, todate):
    df = pd.read_csv(datapath)
    return len(df[(df['trade_date'] >= int(fromdate.strftime('%Y%m%d'))) 
            & (df['trade_date'] <= int(todate.strftime('%Y%m%d')))])
    
# 创建策略
class BollStrategy(bt.Strategy):
    # 可配置策略参数
    params = dict(
        p_period_volume = 10,   # 前n日最大交易量
        p_sell_ma = 5,          # 跌破该均线卖出
        p_oneplot = False,      # 是否打印到同一张图
        pstake = 1000,          # 单笔交易股票数
    )
    def __init__(self):
        self.inds = dict()
        for i, d in enumerate(self.datas):
            self.inds[d] = dict()
            # 布林线中轨
            boll_mid = bt.ind.BBands(d.close).mid
            # 买入条件
            self.inds[d]['buy_con'] = bt.And( \
                # 突破中轨
                d.open < boll_mid, d.close > boll_mid, \
                # 放量
                d.volume == bt.ind.Highest(d.volume, period = self.p.p_period_volume, plot = False))
            # 卖出条件
            self.inds[d]['sell_con'] = d.close < bt.ind.SMA(d.close, period = self.p.p_sell_ma)
            # 跳过第一只股票data，第一只股票data作为主图数据
            if i > 0:
                if self.p.p_oneplot:
                    d.plotinfo.plotmaster = self.datas[0]
    def next(self):
        for i, d in enumerate(self.datas):
            dt, dn = self.datetime.date(), d._name           # 获取时间及股票代码
            pos = self.getposition(d).size
            if not pos:                                      # 不在场内，则可以买入
                if self.inds[d]['buy_con']:                # 如果金叉
                    self.buy(data = d, size = self.p.pstake) # 买买买
            elif self.inds[d]['sell_con']:                  # 在场内，且死叉
                self.close(data = d)                         # 卖卖卖

    def notify_trade(self, trade):
        dt = self.data.datetime.date()
        if trade.isclosed:
            print('{} {} Closed: PnL Gross {}, Net {}'.format(
                dt, trade.data._name, round(trade.pnl, 2), round(trade.pnlcomm, 2)
            ))

cerebro = bt.Cerebro()  

# input stock data
stk_code_file = '/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyData/StockList.csv'
stk_pools = pd.read_csv(stk_code_file)

if stk_num > stk_pools.shape[0]:
    print('number of backtesting stock should not be more than %d' % stk_pools.shape[0])
    exit()
    
#! reading all stock data togather 
for i in range(stk_num):
    stk_code = stk_pools['ts_code'][stk_pools.index[i]]
    
    datapath = '/Users/bowenduan/Applications/OneDrive/200_Knowledge/270_Stock/QT/QuantTrading-/datas/AstockDailyData/' + stk_code + '.csv'
    fromdate=datetime.datetime(2019, 1, 15)
    todate=datetime.datetime(2021, 1, 15)
    
    if MIN_PERIOD > bar_size(datapath, fromdate, todate):
        continue
    
    # read data
    
    data = bt.feeds.GenericCSVData(
        dataname=datapath,
        fromdate=fromdate,
        todate=todate,
        nullvalue=0.0,
        dtformat=('%Y%m%d'),
        datetime=0,
        time=-1,
        high=2,
        low=3,
        open=1,
        close=4,
        volume=6,
        openinterest=-1,
        timeframe=bt.TimeFrame.Days,
    )
    
    # add stock name in cerebro
    cerebro.adddata(data, name = stk_code)


# 设置启动资金
cerebro.broker.setcash(100000.0)
# 设置佣金为千分之一
cerebro.broker.setcommission(commission=0.001)
cerebro.addstrategy(BollStrategy, p_oneplot = False)  # 添加策略
cerebro.run()  # 遍历所有数据
# 打印最后结果
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()  # 绘图

