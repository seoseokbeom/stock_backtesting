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


QQQ = yf.Ticker('QQQ')
qqq = QQQ.history(start="2012-05-01",  end=datetime.today())
qqq = qqq.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    qqq[i] = qqq[i].astype('float64')

# mdd
maxMDD = mdd(qqq)

# import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(x=qqq['Date'],
                                     open=qqq['Open'],
                                     high=qqq['High'],
                                     low=qqq['Low'],
                                     close=qqq['Close'],
                                     )]).update_layout(title_font_size=24)
fig.update_layout(
    title="QQQ mdd:-{}%".format(maxMDD),
    yaxis_title='QQQ Stock',
    shapes=[dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)
fig.update_layout(xaxis_rangeslider_visible=False, yaxis_type="log")
fig.show()
