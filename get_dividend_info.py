import yfinance as yf
from get_all_tickers import get_tickers as gt
from get_all_tickers.get_tickers import Region
import pandas as pd
'''
msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
msft.history_metadata

# show actions (dividends, splits, capital gains)
msft.actions
print(msft.dividends)
msft.splits
msft.capital_gains  # only for mutual funds & etfs


# show financials:
# - income statement
msft.income_stmt
msft.quarterly_income_stmt
# - balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# - cash flow statement
msft.cashflow
msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options


# show news
msft.news
'''

msft = yf.Ticker("MSFT")
#print(msft.info)
msft_info = msft.info
print(msft_info['exDividendDate'])



# tickers of all exchanges
tickers = gt.get_tickers()
print(tickers[:5])

# tickers from NYSE and NASDAQ only
tickers = gt.get_tickers(AMEX=False)