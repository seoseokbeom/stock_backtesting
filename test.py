
import yfinance as yf
import ta
import pandas as pd
from datetime import date, timedelta, datetime
from IPython.display import clear_output

import plotly.graph_objects as go


# warnings.simplefilter(action='ignore', category=FutureWarning)
ticker = 'ISF.L'
start_date = '2019-01-01'
end_date = '2021-01-31'

date_fmt = '%Y-%m-%d'


start_date_buffer = datetime.strptime(
    start_date, date_fmt) - timedelta(days=365)
start_date_buffer = start_date_buffer.strftime(date_fmt)
start_date_buffer

df = yf.download(ticker, start=start_date_buffer, end=end_date)
print(df.head())
# print(df.tail())


def get_stock_backtest_data(ticker, start_date, end_date):
    date_fmt = '%Y-%m-%d'
    start_date_buffer = datetime.strptime(
        start_date, date_fmt) - timedelta(days=365)
    start_date_buffer = start_date_buffer.strftime(date_fmt)

    df = yf.download(ticker, start=start_date_buffer, end=end_date)

    return df


# def price_chart(company):
#     company_nm = dart.company(company)['stock_name']  # 종목명
#     company_nm_eng = dart.company(company)['corp_name_eng']  # 회사 영문명
#     company_stock_code = dart.company(company)['stock_code']  # 종목코드
#     title = company_nm + ' (' + company_nm_eng + \
#         ', ' + company_stock_code + ')'
#     titles = dict(text=title, x=0.5, y=0.85)

#     fig = make_subplots(specs=[[{'secondary_y': True}]])
#     x = price_all(company).index.tolist()
#     y = price_all(company)['Close']
#     fig.add_trace(go.Scatter(mode='lines', name='주가', x=x,  y=y))
#     annotations = []
#     annotations.append(dict(xref='paper', x=0.95, y=y.tail(1)[0],
#                             xanchor='left', yanchor='middle',
#                             text=str(x[-1:])[12:22] + ' : ' +
#                             f'{y.tail(1)[0]:,.0f}',
#                             font=dict(family='Arial', size=12),
#                             showarrow=False))

#     fig.update_layout(title=titles, titlefont_size=15,
#                       legend_title_text='(단위 : 원)', annotations=annotations)
#     fig.show()

df = get_stock_backtest_data('TQQQ', '2019-01-01', '2021-01-31')
fig = go.Figure(data=[go.Candlestick(
    # x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'])])
fig.show()
# TQQ = df['Adj Close']
# print(df['Adj Close'].tail())

# TQQ = tqquvxy['TQQQ']
# UVXY = tqquvxy['UVXY']
# print(TQQ.tail())
