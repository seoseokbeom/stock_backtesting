import yfinance as yf
import pandas as pd
from datetime import date, timedelta, datetime
from IPython.display import clear_output
import matplotlib.pyplot as pp
import plotly.graph_objects as go
from TQQQ_UVXY_MDD import MDDGraph_one, MDDGraph_tow_combination
from MDD import mdd

# total_asset = [1000]
rebalencing_ratio = [9, 1]

SPY = yf.Ticker('SPY')
SPY_date = SPY.history(start="2019-01-02",  end=datetime.today())
spy = SPY_date.reset_index()
spy_close = spy['Close']
spy_close = list(map(lambda x: x/spy_close[0]*1000, spy_close))
# print(spy_close)

FNGU = yf.Ticker('FNGU')
FNGU_date = FNGU.history(start="2019-01-02",  end=datetime.today())
fngu = FNGU_date.reset_index()
fngu_close = fngu['Close']
fngu_close = list(map(lambda x: x/fngu_close[0]*1000, fngu_close))


TQQQ = yf.Ticker('TQQQ')
TQQQ_date = TQQQ.history(start="2019-01-02",  end=datetime.today())
tqqq = TQQQ_date.reset_index()
tqqq_close = tqqq['Close']
tqqq_close2 = list(map(lambda x: x/tqqq_close[0]*1000, tqqq_close))

QQQ = yf.Ticker('QQQ')
qqq_date = QQQ.history(start="2019-01-01",  end=datetime.today())
qqq = qqq_date.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    qqq[i] = qqq[i].astype('float64')
qqq_close = qqq['Close']
qqq_daily_percentage = []
for i in range(1, len(qqq_close)):
    qqq_daily_percentage.append(
        round((qqq_close[i]-qqq_close[i-1])/qqq_close[i-1]+1, 6))


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


QQQ_total_asset = [1000]
tmp2 = QQQ_total_asset[0]
for i in range(len(qqq_daily_percentage)):
    tmp2 = round(tmp2*qqq_daily_percentage[i])
    QQQ_total_asset.append(tmp2)

QQQ_UVXY_total_asset = [1000]
tmp1 = QQQ_UVXY_total_asset[0]
for i in range(len(qqq_daily_percentage)):
    tmp1 = round(tmp1*qqq_daily_percentage[i]
                 * 0.9 + tmp1*uvxy_daily_percentage[i]*0.1)
    QQQ_UVXY_total_asset.append(tmp1)

TQQQ_UVXY_total_asset = [1000]
tmp3 = TQQQ_UVXY_total_asset[0]
for i in range(len(tqqq_daily_percentage)):
    tmp3 = round(tmp3*tqqq_daily_percentage[i]
                 * 0.8 + tmp3*uvxy_daily_percentage[i]*0.2)
    TQQQ_UVXY_total_asset.append(tmp3)


FNGU_UVXY_total_asset = [1000]
tmp3 = FNGU_UVXY_total_asset[0]
for i in range(len(tqqq_daily_percentage)):
    tmp3 = round(tmp3*tqqq_daily_percentage[i]
                 * 0.8 + tmp3*uvxy_daily_percentage[i]*0.2)
    FNGU_UVXY_total_asset.append(tmp3)


QQQ_UVXY_monthly_rebalancing_total_asset = [1000]
tmp3 = QQQ_UVXY_monthly_rebalancing_total_asset[0]
rebalancing_ratio = [0.9, 0.1]
qqqwon = 900
uvxywon = 100
for i in range(len(qqq_daily_percentage)):
    if i % 21 == 0:
        totalamount = qqqwon+uvxywon
        qqqwon = (totalamount)*rebalancing_ratio[0]
        uvxywon = (totalamount)*rebalancing_ratio[1]
    qqqwon = qqqwon*qqq_daily_percentage[i]
    uvxywon = uvxywon*uvxy_daily_percentage[i]
    QQQ_UVXY_monthly_rebalancing_total_asset.append(qqqwon+uvxywon)

UVXY_daily_rebalancing_total_asset = [5000]
tmp4 = UVXY_daily_rebalancing_total_asset[0]
for i in range(len(uvxy_daily_percentage)):
    tmp4 = round(tmp4*uvxy_daily_percentage[i])
    UVXY_daily_rebalancing_total_asset.append(tmp4)


SPY_strategy = go.Scatter(x=qqq['Date'][1:],
                          y=spy_close,
                          )
TQQQ_strategy = go.Scatter(x=qqq['Date'][1:],
                           y=tqqq_close2,
                           )
FNGU_strategy = go.Scatter(x=qqq['Date'][1:],
                           y=fngu_close,
                           )

FNGU_UVXY_daily_rebalancing_strategy = go.Scatter(x=qqq['Date'][1:],
                                                  y=FNGU_UVXY_total_asset,
                                                  )

QQQ_strategy = go.Scatter(x=qqq['Date'][1:],
                          y=QQQ_total_asset,
                          )
QQQ_UVXY_daily_rebalancing_strategy = go.Scatter(x=qqq['Date'][1:],
                                                 y=QQQ_UVXY_total_asset,
                                                 )

QQQ_UVXY_monthly_rebalancing_strategy = go.Scatter(x=qqq['Date'][1:],
                                                   y=QQQ_UVXY_monthly_rebalancing_total_asset,
                                                   )

TQQQ_UVXY_daily_rebalancing_strategy = go.Scatter(x=qqq['Date'][1:],
                                                  y=TQQQ_UVXY_total_asset,
                                                  )
UVXY_daily_rebalancing_strategy = go.Scatter(x=qqq['Date'][1:],
                                             y=UVXY_daily_rebalancing_total_asset,
                                             )


fig = go.Figure(data=[QQQ_strategy,
                      FNGU_strategy, FNGU_UVXY_daily_rebalancing_strategy])
MDDGraph_one('FNGU')
MDDGraph_tow_combination('FNGU', 'UVXY', title='FNGU, UVXY 8:2')
MDDGraph_tow_combination('FNGU', 'BTC-USD', title='FNGU, BTC-USD 8:2')

fig.update_layout(yaxis_type="log")
# xaxis_rangeslider_visible=False,
fig.show()
