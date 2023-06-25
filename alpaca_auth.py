class AlpacaAuth:
    def __init__(self, alpaca_api_key, alpaca_secret_key, alpaca_endpoint):
        self.alpaca_api_key = alpaca_api_key
        self.alpaca_secret_key = alpaca_secret_key
        self.alpaca_endpoint = alpaca_endpoint

alpacaAuth = AlpacaAuth(
    alpaca_api_key="PKLVDOP71I95P0BPWCV5",
    alpaca_secret_key="hOJ8X5GjZhAILeGSBAbvi021uE16bysXtaWts0vA",
    alpaca_endpoint="https://paper-api.alpaca.markets"
)
