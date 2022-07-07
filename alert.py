#from email import message
#from telnetlib import DM
#from aiohttp import payload_type
import ccxt, yfinance, ta
#from config import BINANCE_SECRE_KEY
import pandas_ta as ta
import pandas as pd
import requests

exchange = ccxt.binance()
                        #({
                            #'apiKey': config.BINANCE_API_KEY,
                            #'secret': config.BINANCE_SECRE_KEY
                         #})

bars = exchange.fetch_ohlcv('ETH/USDT', timeframe = '5m', limit = 500)
df = pd.DataFrame(bars [:-1],columns=['time','open','high', 'low','close','volume'])
adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()
df = pd.concat([df, adx, macd, rsi], axis = 1)

last_row = df.iloc[-1] #last row of the dataset
#print(last_row)

WEBHOOK_URL = "https://discordapp.com/api/webhooks/993964755851161642/KBUAyEhJC0rsXSKA7cPtks01cOYxuN7h2q6gQ2YXQvRMJspp9-t2qqCCQ1L3-ojzP2nG"


if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: The ADX is {last_row['ADX_14']:.2f}"
    if last_row['DMN_14'] > last_row['DMP_14']:
        message = f"STRONG DOWNTREND: The ADX is {last_row['ADX_14']:.2f}"

if last_row['ADX_14'] < 25:
    message = f"NO TREND: The ADX is {last_row['ADX_14']:.2f}"

print(message)

payload = {
    "username": "alertbot",
    "content": message
    }
requests.post(WEBHOOK_URL, json=payload)

