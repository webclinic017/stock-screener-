import pandas as pd

class StockScreener:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def filter_stocks(self):
        volatile_stocks = self._get_volatile_stocks()
        return volatile_stocks

    def _get_volatile_stocks(self):
        stock_volatility = self.stock_data["Close"].pct_change().std() * (252 ** 0.5)
        volatile_stocks = stock_volatility.nlargest(10)
        return volatile_stocks
