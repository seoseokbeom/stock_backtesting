import yfinance as yf
import ta
import pandas as pd
from datetime import date, timedelta, datetime
from IPython.display import clear_output
import matplotlib.pyplot as pp
import plotly.graph_objects as go
from MDD import mdd


def get_stock_backtest_data(ticker, start_date, end_date):
    date_fmt = '%Y-%m-%d'
    start_date_buffer = datetime.strptime(
        start_date, date_fmt) - timedelta(days=365)
    start_date_buffer = start_date_buffer.strftime(date_fmt)

    df = yf.download(ticker, start=start_date_buffer, end=end_date)

    return df


UVXY = yf.Ticker('UVXY')
uvxy = UVXY.history(start="2012-05-01",  end=datetime.today())
uvxy = uvxy.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    uvxy[i] = uvxy[i].astype('float64')
# import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(x=uvxy['Date'],
                                     open=uvxy['Open'],
                                     high=uvxy['High'],
                                     low=uvxy['Low'],
                                     close=uvxy['Close'])])
fig.update_layout(xaxis_rangeslider_visible=False, yaxis_type="log")
fig.show()

mdd(uvxy)
