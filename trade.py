# Import the necessary libraries
import backtrader as bt
import mt5
import pandas as pd

# Connect to the MT5 trading platform
mt5.initialize()

# Set the EURUSD symbol and time frame
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H4

# Download the historical data for EURUSD
eurusd_data = mt5.copy_rates_from_pos(symbol, timeframe, 0, 365 * 24)

# Convert the data to a Pandas DataFrame with the correct column names
eurusd_data = pd.DataFrame(eurusd_data, columns=["time", "open", "high", "low", "close", "tick_volume", "spread", "real_volume"])

# Set the trading parameters
lot = 1.0
take_profit = 100.0
stop_loss = 50.0


# Create a subclass of the Backtrader Strategy class
class MyStrategy(bt.Strategy):
    def __init__(self):
        # Create a Moving Average CrossOver indicator
        self.maco = bt.indicators.MovingAverageCross()

        # Create a Relative Strength Index indicator
        self.rsi = bt.indicators.RSI()

        # Create a Moving Average Convergence Divergence indicator
        self.macd = bt.indicators.MACD()

    def next(self):
        if not self.position:
            # Check if a long position should be opened
            if self.maco > 0 and self.rsi < 30 and self.macd > 0:
                # Open a long position on EURUSD
                self.buy(symbol=symbol, volume=lot,
                         exectype=bt.Order.Market,
                         transmit=False)

        else:
            # Check if the long position should be closed
            if self.maco < 0 or self.rsi > 70 or self.macd < 0:
                # Close the long position on EURUSD
                self.sell(symbol=symbol, volume=lot,
                         exectype=bt.Order.Market,
                         transmit=False)


# Create a Backtrader cerebro instance
cerebro = bt.Cerebro()

# Load the historical data for the EURUSD currency pair
data = bt.feeds.PandasData(dataname=eurusd_data)

# Add the data to the cerebro instance
cerebro.adddata(data)

# Set the starting cash balance
cerebro.broker.setcash(100000.0)

# Add the MyStrategy subclass to cerebro
cerebro.addstrategy(MyStrategy)

# Perform optimization on the strategy
maperiod1_values = range(10, 100)
maperiod2_values = range(10, 100)
rsiperiod_values = range(10, 100)

cerebro.optstrategy(
    MyStrategy,
    maperiod1=maperiod1_values,
    maperiod2=maperiod2_values,
    rsiperiod=rsiperiod_values
)

# Run the backtest
results = cerebro.run()

# Print the backtest results
print("Backtest results:")
print(results)
