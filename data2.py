import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import os

if not mt5.initialize():
    print ("not working mt4 ")
    quit()
    
symbolse = ["BTCUUSDM","XAUUSDm"]
csv_folder = "symbal data"
dates = []

account = mt5.account_info()
if account is not None:
    print(f"Login: {account.login}")
    print(f"Balance: {account.balance}")
    print(f"Equity: {account.equity}")
else:
    print("⚠ Account info not available")

# dates.append(account)

for symbal in symbolse:
    tick = mt5.symbol_info_tick(symbal)
data = {
    "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "symbales": symbolse,
    "bid": tick.bid,
    
    "login": account.login,
    "name": account.name,
    "server": account.server,
    "balance": account.balance,
    "equity": account.equity,
    "margin": account.margin,
    "margin_free": account.margin_free,
    "profit": account.profit
}
dates.append(data)
print(f"Data collected for = {symbolse}: {data}")
    
mt5.shutdown()  

if dates:
    df = pd.DataFrame(dates)
    
    file_exists = os.path.isfile(csv_folder)
    df.to_csv(csv_folder, mode='a', header=not file_exists, index=False)
else:
    print("No data collected.")
