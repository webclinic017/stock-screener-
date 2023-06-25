class FinancialRatios:
    def price_to_earnings(self, data):
        pe_ratio = data['Close'] / data['EarningsPerShare']
        return pe_ratio

    def return_on_equity(self, data):
        roe = data['NetIncome'] / data['ShareholdersEquity']
        return roe

    def debt_to_equity(self, data):
        debt_equity_ratio = data['TotalDebt'] / data['ShareholdersEquity']
        return debt_equity_ratio

    def earnings_per_share(self, data):
        eps = data['EarningsPerShare']
        return eps

    def price_to_sales(self, data):
        ps_ratio = data['MarketCap'] / data['Revenue']
        return ps_ratio
