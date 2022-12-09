# MT5 EURUSD Trading Bot

This is a Python trading bot that uses the `mt5` library and the `backtrader` library to trade the EURUSD currency pair on the MT5 platform. The bot uses a simple moving average crossover strategy with the RSI and MACD indicators for entry and exit signals.

## Requirements

- The `mt5` library (version 5.0 or higher)
- The `backtrader` library (version 1.9.74.123 or higher)
- A MT5 trading account with EURUSD as a available trading instrument

## Usage
1. Import the necessary libraries: import backtrader as bt, import mt5, and import pandas as pd
2. Initialize the MT5 library by calling mt5.initialize()
3. Set the symbol variable to the currency pair that you want to trade (e.g. "EURUSD") and the timeframe variable to the time frame that you want to use (e.g. mt5.TIMEFRAME_H4 for 4-hour candles)
4. Download the historical data for the currency pair by calling mt5.copy_rates_from_pos(symbol, timeframe, 0, 365 * 24)
5. Convert the historical data to a Pandas DataFrame with the correct column names (e.g. eurusd_data = pd.DataFrame(eurusd_data, columns=["time", "open", "high", "low", "close", "tick_volume", "spread", "real_volume"]))
6. Set the trading parameters, such as the lot size, take profit level, and stop loss level
7. Create a subclass of the bt.Strategy class and implement your trading strategy in the next() method. In this example, the next() method contains the logic for the moving average crossover strategy with the RSI and MACD indicators.
8. Create a bt.Cerebro instance and add the historical data, trading strategy, and starting cash balance. You can also specify the parameters for the moving average, RSI, and MACD indicators in the cerebro.addstrategy() method.
9. Run the trading bot by calling cerebro.run()

