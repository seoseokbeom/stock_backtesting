import yfinance as yf
import ta
import pandas as pd
from datetime import date, timedelta, datetime
from IPython.display import clear_output
import matplotlib.pyplot as pp
import plotly.graph_objects as go
from MDD import mdd

# End=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')


def dailyPercentage(ticker, Start="2019-01-01", End=datetime.today()):
    ticker_yf = yf.Ticker(ticker)
    ticker_date = ticker_yf.history(start=Start,  end=End)
    ticker_yf = ticker_date.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']:
        ticker_yf[i] = ticker_yf[i].astype('float64')
    ticker_close = ticker_yf['Close']
    ticker_daily_percentage = []
    for i in range(1, len(ticker_close)):
        ticker_daily_percentage.append(
            round((ticker_close[i]-ticker_close[i-1])/ticker_close[i-1]+1, 6))
    return ticker_daily_percentage, ticker_yf


def MDDGraph_one(ticker, Start="2019-01-01", End=datetime.today()):
    ticker_tmp = yf.Ticker(ticker)
    ticker2 = ticker_tmp.history(start=Start,  end=End)
    ticker2 = ticker2.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']:
        ticker2[i] = ticker2[i].astype('float64')
    return mdd(ticker2, ticker)


def MDDGraph_tow_combination(ticker1, ticker2, title="TITLE", rebalancing_ratio=(9, 1), Start="2019-01-01", End=datetime.today()):
    combined_ticker_total_asset = [1000]
    tmp1 = combined_ticker_total_asset[0]
    tickerA_daily_percentage, ticker1_date = dailyPercentage(
        ticker1, Start, End)
    tickerB_daily_percentage, ticker2_date = dailyPercentage(
        ticker2, Start, End)
    # for i in range(len(ticker2_daily_percentage)):
    #     tmp1 = round(
    #         tmp3*ticker1_daily_percentage[i] * ratio[0] + tmp3*ticker2_daily_percentage[i]*ratio[1])
    #     total_asset.append(tmp1)
    # total_asset = pd.DataFrame(total_asset,   columns=['Close'])
    # maxMDD = mdd(total_asset, title)

    i, j = 0, 0
    while i < len(tickerA_daily_percentage) and j < len(tickerB_daily_percentage):
        if i >= len(tickerA_daily_percentage) or j >= len(tickerB_daily_percentage):
            break
        if ticker1_date['Date'][i] == ticker2_date['Date'][j]:
            # print('same')
            tmp1 = round(tmp1*tickerA_daily_percentage[i]
                         * rebalancing_ratio[0]/sum(rebalancing_ratio) + tmp1*tickerB_daily_percentage[j]*rebalancing_ratio[1]/sum(rebalancing_ratio), 4)
            combined_ticker_total_asset.append(tmp1)
            i += 1
            j += 1
        else:
            # print('diff')
            if ticker1_date['Date'][i] > ticker2_date['Date'][j]:
                tmp1 = round(tmp1 * tickerB_daily_percentage[j], 4)
                combined_ticker_total_asset.append(tmp1)
                j += 1
            else:
                tmp1 = round(tmp1*tickerA_daily_percentage[i], 4)
                combined_ticker_total_asset.append(tmp1)
                i += 1
    combined_ticker_total_asset = pd.DataFrame(
        combined_ticker_total_asset,   columns=['Close'])
    maxMDD = mdd(combined_ticker_total_asset, title)
    return maxMDD
    # print(tmp1)

    # TQQQ_UVXY_total_asset = [1000]
    # tmp3 = TQQQ_UVXY_total_asset[0]
    # for i in range(len(tqqq_daily_percentage)):
    #     tmp3 = round(tmp3*tqqq_daily_percentage[i]
    #                 * 0.8 + tmp3*uvxy_daily_percentage[i]*0.2)
    #     TQQQ_UVXY_total_asset.append(tmp3)

    # TQQQ_UVXY_total_asset = pd.DataFrame(
    #     TQQQ_UVXY_total_asset,   columns=['Close'])


TQQQ = yf.Ticker('TQQQ')
tqqq_date = TQQQ.history(start="2019-01-01",  end=datetime.today())
tqqq = tqqq_date.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    tqqq[i] = tqqq[i].astype('float64')
tqqq_close = tqqq['Close']
tqqq_daily_percentage = []
for i in range(1, len(tqqq_close)):
    tqqq_daily_percentage.append(
        round((tqqq_close[i]-tqqq_close[i-1])/tqqq_close[i-1]+1, 6))


UVXY = yf.Ticker('UVXY')
uvxy = UVXY.history(start="2019-01-01",  end=datetime.today())
uvxy = uvxy.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    uvxy[i] = uvxy[i].astype('float64')
uvxy = uvxy['Close']
uvxy_daily_percentage = []
for i in range(1, len(uvxy)):
    uvxy_daily_percentage.append(round((uvxy[i]-uvxy[i-1])/uvxy[i-1]+1, 6))


TQQQ_UVXY_total_asset = [1000]
tmp3 = TQQQ_UVXY_total_asset[0]
for i in range(len(tqqq_daily_percentage)):
    tmp3 = round(tmp3*tqqq_daily_percentage[i]
                 * 0.8 + tmp3*uvxy_daily_percentage[i]*0.2)
    TQQQ_UVXY_total_asset.append(tmp3)

TQQQ_UVXY_total_asset = pd.DataFrame(
    TQQQ_UVXY_total_asset,   columns=['Close'])
# mdd
# maxMDD = mdd(TQQQ_UVXY_total_asset)

# import plotly.graph_objects as go
# fig = go.Figure(data=[go.Candlestick(x=qqq['Date'],
#                                      open=qqq['Open'],
#                                      high=qqq['High'],
#                                      low=qqq['Low'],
#                                      close=qqq['Close'],
#                                      )]).update_layout(title_font_size=24)
# fig.update_layout(
#     title="QQQ mdd:-{}%".format(maxMDD),
#     yaxis_title='QQQ Stock',
#     shapes=[dict(
#         x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
#         line_width=2)],
#     annotations=[dict(
#         x='2016-12-09', y=0.05, xref='x', yref='paper',
#         showarrow=False, xanchor='left', text='Increase Period Begins')]
# )
# fig.update_layout(xaxis_rangeslider_visible=False, yaxis_type="log")
# fig.show()
