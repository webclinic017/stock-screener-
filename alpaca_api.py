import alpaca_trade_api as tradeapi
import requests
from alpaca_auth import alpacaAuth

class AlpacaAPI:
    def __init__(self):
        self.alpaca_api_key = alpacaAuth.alpaca_api_key
        self.alpaca_secret_key = alpacaAuth.alpaca_secret_key
        self.alpaca_endpoint = alpacaAuth.alpaca_endpoint
        self.authenticate()
  
    def authenticate(self):
        try:
            self.api = tradeapi.REST(self.alpaca_api_key, self.alpaca_secret_key, self.alpaca_endpoint, api_version='v2')
            return self.api
        except Exception as e:
            # Handle authentication error
            print("Authentication failed:", str(e))
            return None


    def get_market_status(self):
        # Retrieve the current market status (open or closed)
        url = "https://api.alpaca.markets/v2/clock"
        response = requests.get(self.alpaca_api_key, self.alpaca_secret_key, url, api_version='v2')
        if response.status_code == 200:
            market_status = response.json()["is_open"]
            return True
        else:
            return False

    def get_account_information(self):
        #Retrieve the user's account information
        try:
            account = self.api.get_account()
            return account
        except Exception as e:
            # Handle API error
            print("Failed to retrieve account information:", str(e))
            return None
        