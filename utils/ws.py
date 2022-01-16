import hmac
import json
import time
import websockets

class WSClient:
    def __init__(self, api_key, api_secret):
      self.url = "wss://stream.bybit.com/realtime"
      self.api_key = api_key
      self.api_secret = api_secret
      self.alive = False
      self._authenticate()
    
    def _authenticate():
        print("let's do this later")