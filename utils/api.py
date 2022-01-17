import requests
import numpy
import pandas as pd

class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'
    
    def intraday_query(self, symbol, market, interval, output_size):
        api_url = f'{self.base_url}?function=CRYPTO_INTRADAY&symbol={symbol}&market={market}&interval={interval}&outputsize={output_size}&apikey={self.api_key}'
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['Time Series Crypto ('+interval+')']).T
        for i in df.columns:
            df[i] = df[i].astype(float)
        df.index = pd.to_datetime(df.index)
        return df
        