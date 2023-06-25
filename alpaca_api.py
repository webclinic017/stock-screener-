import alpaca_trade_api as tradeapi
import requests
from alpaca_auth import alpacaAuth

class AlpacaAPI:
    def __init__(self, endpoint, key, secret):
        alpaca_api_key = alpacaAuth.alpaca_api_key
        alpaca_secret_key = alpacaAuth.alpaca_secret_key
        alpaca_endpoint = alpacaAuth.alpaca_endpoint
        self.api = tradeapi.REST(alpaca_api_key, alpaca_secret_key, alpaca_endpoint, api_version='v2')

    def authenticate(self):
        # Authenticate the user with the Alpaca API
        pass

    def get_market_status(self):
        # Retrieve the current market status (open or closed)
        url = "https://api.alpaca.markets/v2/clock"
        response = requests.get(url)
        if response.status_code == 200:
            market_status = response.json()["is_open"]
            return True
        else:
            return False

    def get_account_information(self):
        # Retrieve the user's account information
        pass



test = AlpacaAPI()
print(test.get_market_status())