import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import os

#------------------------------------------------------------------------------------------------------------------------------
if not mt5.initialize():
    print("*********** MT5 initialization failed:", mt5.last_error())
    quit()

symbols = ["XAUUSDm"] 
csv_file = "gold_rates.csv"
data_list = []

print(f" Step 2: Target symbols = {symbols}")


for symbol in symbols:

    if not mt5.symbol_select(symbol, True):
        print(f"!********* Failed to select symbol: {symbol}")
        continue

  
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"***** No tick data for: {symbol}")
        continue
    print(f" Tick data received: {tick}")

   
    tick_time = datetime.fromtimestamp(tick.time)

  
    data = {
        "datetime": tick_time.strftime('%Y-%m-%d %H:%M:%S'),
        "symbol": symbol,
        "bid": tick.bid,
        "ask": tick.ask,
       # "last": tick.last,
       # "volume": tick.volume
    }
    data_list.append(data)
    print(f" Data collected for = {symbol}: {data}")
     
mt5.shutdown()

## Save data to CSV file-------------------------------------------------------------------------------------------------------------

if data_list:
    df = pd.DataFrame(data_list)

    file_exists = os.path.isfile(csv_file)

  
    df.to_csv(csv_file, mode='a', header=not file_exists, index = False)
    print(f" =============Data saved to {csv_file}")
else:
    print("********************** No data collected.")
