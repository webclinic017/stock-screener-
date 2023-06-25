import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

class StockDataFetcher:
    def __init__(self):
        self.base_url = "https://finviz.com/screener.ashx?v=111&f=ind_technology"

    def get_stock_data(self):
        stock_symbols = self._get_stock_symbols_from_finviz()
        stock_data = self._get_stock_data_from_yahoo(stock_symbols)
        return stock_data

    def _get_stock_symbols_from_finviz(self):
        stock_symbols = []
        page = 1
        while True:
            url = f"{self.base_url}&r={page}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", class_="screener-body-table-nw")
            if table is None:
                break
            rows = table.find_all("tr")
            for row in rows:
                symbol = row.find("a", class_="screener-link-primary")
                if symbol:
                    stock_symbols.append(symbol.text)
            page += 20
        return stock_symbols

    def _get_stock_data_from_yahoo(self, stock_symbols):
        stock_data = yf.download(stock_symbols, period="1d", group_by="ticker")
        return stock_data


test = StockDataFetcher()
print(test.get_stock_data())
