import yfinance as yf
from get_all_tickers import get_tickers as gt
from get_all_tickers.get_tickers import Region
import pandas as pd
from datetime import datetime#
import time 
div_min = 0.1
div_data = pd.read_csv('dividend_table.csv')
unix_timestamp = datetime.now()
other_time_stamp = time.time()
print(unix_timestamp)
print(other_time_stamp)
#print(div_data)
div_data = div_data.dropna()
print(div_data)
div_data = div_data.query('Dividend_Yield > @div_min' and 'UNIX_Div_Date > @other_time_stamp')
print(div_data)
div_data = div_data.sort_values(by=['UNIX_Div_Date'], ascending=True)
div_data.to_csv('filtered_div_data.csv')




