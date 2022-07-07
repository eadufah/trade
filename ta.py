import ccxt, yfinance, ta
#from config import BINANCE_SECRE_KEY
import pandas_ta as ta
import pandas as pd

exchange = ccxt.binance()
                        #({
                            #'apiKey': config.BINANCE_API_KEY,
                            #'secret': config.BINANCE_SECRE_KEY
                         #})

#markets = exchange.load_markets
bars = exchange.fetch_ohlcv('ETH/USDT', timeframe = '5m', limit = 20)
df = pd.DataFrame(bars [:-1],columns=['time','open','high', 'low','close','volume'])

adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

df = pd.concat([df, adx, macd, rsi], axis = 1)
#df = df[df['RSI_14']<30]

#last_row = df.iloc[-1]
#print(df)



