import yfinance as yf
import datetime as dt
import pandas as pd

stocks = ['AMZN', 'NIO', 'ASML', 'WMT', 'TSM', 'KO', 'COST', 'TAL', 'NKE', 'BILI',
          'PDD', 'NVDA', 'NVDA']

start = dt.datetime.today()-dt.timedelta(360)
end = dt.datetime.today()

cl_price = pd.DataFrame()
ohcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)['Adj Close']

for ticker in stocks:
    ohcv_data[ticker] = yf.download(ticker, start, end)

# ohcv_data['AMZN']['Open']
