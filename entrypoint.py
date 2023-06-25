import alpaca_trade_api as tradeapi
from stock_screener import StockScreener
from alpaca_auth import alpacaAuth


if __name__ == "__main__":
    alpaca_api_key = alpacaAuth.alpaca_api_key
    alpaca_secret_key = alpacaAuth.alpaca_secret_key
    alpaca_endpoint = alpacaAuth.alpaca_endpoint

    api = tradeapi.REST(alpaca_api_key, alpaca_secret_key, alpaca_endpoint, api_version='v2')

    screener = StockScreener(api)
    screener.run()
