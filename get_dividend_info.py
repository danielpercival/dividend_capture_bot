import yfinance as yf
from get_all_tickers import get_tickers as gt
from get_all_tickers.get_tickers import Region
import pandas as pd
from datetime import datetime
from IPython.display import display
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
df = pd.read_csv('ticker_list')
list_of_tickers = list(df['Tickers'])

all_tickers = yf.Tickers(list_of_tickers)
dividend_df = pd.DataFrame(columns=['Ticker','Price_to_Earnings','Dividend_Yield','Dividend_Date', 'UNIX_Div_Date'])
#display(dividend_df)
for i in list_of_tickers:
    try:
        
        print('the current stock is: ', i)
        stock = yf.Ticker(i)
        stock_info = stock.info
        
        try:
            PE_ratio = stock_info['trailingPE']
        except:
            PE_ratio = 'NULL'
        try:
            exDivDateUnix = int(stock_info['exDividendDate'])
            exDivDate = datetime.utcfromtimestamp(exDivDateUnix).strftime('%d-%m-%Y')
            last_Div_Value = stock_info['lastDividendValue']
            last_div_date = stock_info['lastDividendDate']
            payout_ratio = stock_info['payoutRatio']
            div_yield = stock_info['dividendYield']
            div_rate = stock_info['dividendRate']
        except: 
            last_Div_Value = last_div_date = payout_ratio = div_yield = div_rate = exDivDateUnix = exDivDate = 'NULL'

        data = [[i, PE_ratio, div_yield, exDivDate, exDivDateUnix]]
        dividend_temp_df = pd.DataFrame(data, columns=['Ticker','Price_to_Earnings','Dividend_Yield','Dividend_Date', 'UNIX_Div_Date'])
        print('temp div df is: ', dividend_temp_df)
        dividend_df = pd.concat([dividend_df, dividend_temp_df])
    except:
        print('there has been a failure')
        pass


print('final df is: ', dividend_df)
display(dividend_df)
dividend_df.to_csv('dividend_table.csv', index= False)
'''
msft = yf.Ticker("MSFT")
#print(msft.info)
msft_info = msft.info
print(msft_info['exDividendDate'])
exDivDateUnix = int(msft_info['exDividendDate'])
print(datetime.utcfromtimestamp(exDivDateUnix).strftime('%d-%m-%Y'))

all_tickers_info = all_tickers.info

'''