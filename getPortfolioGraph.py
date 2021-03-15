import yfinance as yf
import pandas as pd
from datetime import date, timedelta, datetime
from IPython.display import clear_output
import matplotlib.pyplot as pp
import plotly.graph_objects as go
from TQQQ_UVXY_MDD import MDDGraph_one, MDDGraph_tow_combination
from MDD import mdd


def onlyOneTickerDailyRebalancing(ticker1, Start="2019-01-01", End=datetime.today()):
    tickerA = yf.Ticker(ticker1)
    tickerA_date = tickerA.history(
        start=Start,  end=End)
    tickerA_ = tickerA_date.reset_index()
    tickerA_close = tickerA_['Close']
    tickerA_close = list(
        map(lambda x: x/tickerA_close[0]*1000, tickerA_close))
    # print(tickerA_close)
    return tickerA_close, tickerA_


def combineTwoTickerDailyRebalancing(ticker1, ticker2, rebalencing_ratio=(0.9, 0.1), Start="2019-01-01", End=datetime.today()):
    tickerA = yf.Ticker(ticker1)
    tickerA_date = tickerA.history(start=Start,  end=datetime.today())
    tickerAA = tickerA_date.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']:
        tickerAA[i] = tickerAA[i].astype('float64')
    tickerA_close = tickerAA['Close']
    tickerA_daily_percentage = []
    for i in range(1, len(tickerA_close)):
        tickerA_daily_percentage.append(
            round((tickerA_close[i]-tickerA_close[i-1])/tickerA_close[i-1]+1, 6))

    tickerB = yf.Ticker(ticker2)
    tickerB_date = tickerB.history(start=Start,  end=datetime.today())
    tickerBB = tickerB_date.reset_index()
    # print('tickerBB  Before:', tickerBB)
    for i in ['Open', 'High', 'Close', 'Low']:
        tickerBB[i] = tickerBB[i].astype('float64')
    # print('tickerBB:', tickerBB)
    tickerB_close = tickerBB['Close']
    # tickerB_date =
    tickerB_daily_percentage = []
    for i in range(1, len(tickerB_close)):
        tickerB_daily_percentage.append(
            round((tickerB_close[i]-tickerB_close[i-1])/tickerB_close[i-1]+1, 6))

    combined_ticker_total_asset = [1000]
    tmp1 = combined_ticker_total_asset[0]
    i, j = 0, 0
    while i < len(tickerA_daily_percentage) and j < len(tickerB_daily_percentage):
        if i >= len(tickerA_daily_percentage) or j >= len(tickerB_daily_percentage):
            break
        if tickerAA['Date'][i] == tickerBB['Date'][j]:
            # print('same')
            tmp1 = round(tmp1*tickerA_daily_percentage[i]
                         * rebalencing_ratio[0]/sum(rebalencing_ratio) + tmp1*tickerB_daily_percentage[j]*rebalencing_ratio[1]/sum(rebalencing_ratio), 4)
            combined_ticker_total_asset.append(tmp1)
            i += 1
            j += 1
        else:
            # print('diff')
            if tickerAA['Date'][i] > tickerBB['Date'][j]:
                tmp1 = round(tmp1 * tickerB_daily_percentage[j], 4)
                combined_ticker_total_asset.append(tmp1)
                j += 1
            else:
                tmp1 = round(tmp1*tickerA_daily_percentage[i], 4)
                combined_ticker_total_asset.append(tmp1)
                i += 1
        # print(tmp1)
    if len(tickerA_daily_percentage) > len(tickerB_daily_percentage):
        return combined_ticker_total_asset, tickerAA
    else:
        return combined_ticker_total_asset, tickerBB


def getGraph(tickerArray,   Start="2019-01-01", End=datetime.today(), title="TITLE"):
    Array = []
    for v in (tickerArray):
        if isinstance(v, str):
            tmp1_close, tmp1_date_reset_idx = onlyOneTickerDailyRebalancing(
                v, Start=Start, End=datetime.today())
            Name = str(v)
        else:
            ticker1, ticker2, rebalancing_ratio = v
            tmp1_close, tmp1_date_reset_idx = combineTwoTickerDailyRebalancing(
                ticker1, ticker2, rebalancing_ratio, Start=Start, End=datetime.today())
            Name = '{}, {} {}'.format(ticker1, ticker2, rebalancing_ratio)

        tmp1_strategy = go.Scatter(x=tmp1_date_reset_idx['Date'][1:],
                                   y=tmp1_close,
                                   name=Name
                                   )
        Array.append(tmp1_strategy)
    print('Array', Array)

    fig = go.Figure(data=Array)
    fig.update_layout(yaxis_type="log")
    # xaxis_rangeslider_visible=False,
    fig.show()


def getGraphWithMdd(tickerArray,  Start="2019-01-01", End=datetime.today(), title="TITLE"):
    Array = []
    for v in (tickerArray):
        if isinstance(v, str):
            tmp1_close, tmp1_date_reset_idx = onlyOneTickerDailyRebalancing(
                v, Start=Start, End=datetime.today())
            MDD = MDDGraph_one(v, Start=Start)
            Name = '{} | MDD:{}%'.format(str(v), MDD)
        else:
            ticker1, ticker2, rebalancing_ratio = v
            tmp1_close, tmp1_date_reset_idx = combineTwoTickerDailyRebalancing(
                ticker1, ticker2, rebalancing_ratio, Start=Start, End=datetime.today())
            print(rebalancing_ratio)
            MDD = MDDGraph_tow_combination(ticker1, ticker2, title='{}, {} {} '.format(
                ticker1, ticker2, rebalancing_ratio), rebalancing_ratio=rebalancing_ratio, Start=Start)
            Name = '{}, {} {} | MDD:{}%'.format(
                ticker1, ticker2, rebalancing_ratio, MDD)

        tmp1_strategy = go.Scatter(x=tmp1_date_reset_idx['Date'][1:],
                                   y=tmp1_close,
                                   name=Name
                                   )
        Array.append(tmp1_strategy)
    print('Array', Array)

    fig = go.Figure(data=Array)
    fig.update_layout(yaxis_type="log")
    fig.show()
