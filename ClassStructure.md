## Cerebro
cerebro = bt.Cerebro(**kwarg)
cerebro.run()


## Data Feed
data = bt.BacktraderCSVData(dataname,fromdate,todate,timeframe)
cerebro.adddata()
cerebro.resampledata()
cerebro.replaydata()

## Add Strategy
cerebro.addstrategy(MyStrategy, myparam1=value1, myparam2=value2)
cerebro.optstrategy(MyStrategy,myparam1=range(1,20))

## Addwriter
addanalyzer
addoberver 

## Broker
broker = MyBroker()
cerebro.broker = broker

## Recieve Information 
callback(msg,*args,**kwargs)

## Standard Observe 
cerebro (unless otherwise specified) automatically instantiates three standard observers\
\*A Broker observer which keeps track of cash and value (portfolio)\
\*A Trades observer which should show how effective each trade has been\
\*A Buy/Sell observer which should document when operations are executed
Should a cleaner plotting be wished just disable them with stdstats=False

## Rertun Resluts
results = cerebro.run(**kwarg)

## Accessing plotting 
cerebro.plot() 