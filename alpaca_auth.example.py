class AlpacaAuth:
    def __init__(self, alpaca_api_key, alpaca_secret_key, alpaca_endpoint):
        self.alpaca_api_key = alpaca_api_key
        self.alpaca_secret_key = alpaca_secret_key
        self.alpaca_endpoint = alpaca_endpoint

alpacaAuth = AlpacaAuth(
    alpaca_api_key="YOUR-API-KEY",
    alpaca_secret_key="YOUR-SECRET-KEY",
    alpaca_endpoint="https://paper-api.alpaca.markets" #endpoint live or paper
)
