import datetime
import backtrader as bt
from strategies import *

# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Set data parameters and add to Cerebro
data = bt.feeds.YahooFinanceData(
    dataname='TSLA',
    fromdate=datetime.datetime(2020, 1, 1),
    todate=datetime.datetime(2020, 12, 12),
)
# settings for out-of-sample data
# fromdate=datetime.datetime(2018, 1, 1),
# todate=datetime.datetime(2019, 12, 25))

cerebro.adddata(data)

# Add strategy to Cerebro
cerebro.addstrategy(TestStrategy)

# Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

if __name__ == '__main__':
    # Run Cerebro Engine
    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run()

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')