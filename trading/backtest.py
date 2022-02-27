import pandas as pd
import numpy as np
import mplfinance as mpf

class Backtester:
    def __init__(self, client, initial_balance=1000):
        self.client = client
        self.initial_balance = initial_balance
        live_data = self._load_1min_data(True, "./btcusd.csv")
        data = self.client.macro_query('BTC', 'USD', 'Daily', start_date = '2021-07-01')
        print(data)
        self._get_levels(data)
        self.plot_levels(data)
        
    def _load_1min_data(self, local, path):
        if local:
            df = pd.read_csv(path)
        
        # get last 6 months of 1 minute
        df = df.sort_values(by='time', ascending=False)
        df = df.head(262800)
        
        return df

    def _get_levels(self, data):
        lows = pd.DataFrame(data=data, index=data.index, columns=["low"])
        highs = pd.DataFrame(data=data, index=data.index, columns=["high"])

        low_clusters = get_optimum_clusters(lows)
        low_centers = low_clusters.cluster_centers_
        low_centers = np.sort(low_centers, axis=0)

        high_clusters = get_optimum_clusters(highs)
        high_centers = high_clusters.cluster_centers_
        high_centers = np.sort(high_centers, axis=0)

        self.lows = low_centers.flatten()
        self.lows = list(self.lows)
        self.highs = high_centers.flatten()
        self.highs = list(self.highs)
        self.pivots = self.lows + self.highs
    
    def plot_levels(self, data):
       mpf.plot(data, hlines=self.pivots)