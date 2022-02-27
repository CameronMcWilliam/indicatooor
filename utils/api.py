import requests
import numpy
import pandas as pd
from pybit import HTTP

class Client:
    def __init__(self, api_key, bybit_api, bybit_secret):
        self.api_key = api_key
        self.bybit_api = bybit_api
        self.bybit_secret = bybit_secret
        self.base_url = 'https://www.alphavantage.co/query?function='
        self.bybit_url = 'https://api.bybit.com'
    
    def intraday_query(self, symbol, market, interval, output_size):
        api_url = f'{self.base_url}CRYPTO_INTRADAY&symbol={symbol}&market={market}&interval={interval}&outputsize={output_size}&apikey={self.api_key}'
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['Time Series Crypto ('+interval+')']).T
        for i in df.columns:
            df[i] = df[i].astype(float)
        df.index = pd.to_datetime(df.index)
        return df

    def macro_query(self, symbol, market, interval, start_date=None):
        up_interval = interval.upper()
        api_url = f'{self.base_url}DIGITAL_CURRENCY_{up_interval}&symbol={symbol}&market={market}&apikey={self.api_key}'
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['Time Series (Digital Currency '+interval+')']).T
        df = df.rename(columns = {'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low', '4a. close (USD)': 'close', '5. volume': 'volume'})
        for i in df.columns:
            df[i] = df[i].astype(float)
        df.index = pd.to_datetime(df.index)
        df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis = 1)
        if start_date:
            df = df[df.index >= start_date]
        return df
    
    def get_pos(self):
        session = HTTP("https://api.bybit.com",
               api_key=self.bybit_api, api_secret=self.bybit_secret)
        print(session.my_position(
        symbol="BTCUSDT"
        ))