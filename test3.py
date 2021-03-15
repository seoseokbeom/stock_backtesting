import yfinance as yf
import pandas as pd
from datetime import date, timedelta, datetime
from IPython.display import clear_output
import matplotlib.pyplot as pp
import plotly.graph_objects as go
from MDD import mdd

total_asset = [1000]
rebalencing_ratio = [9, 1]


QQQ = yf.Ticker('QQQ')
qqq = QQQ.history(start="2020-01-01",  end=datetime.today())
qqq = qqq.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    qqq[i] = qqq[i].astype('float64')
print(qqq[:10])

UVXY = yf.Ticker('UVXY')
uvxy = UVXY.history(start="2020-01-01",  end=datetime.today())
uvxy = uvxy.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    uvxy[i] = uvxy[i].astype('float64')
uvxy = uvxy['Close']
uvxy_daily_percentage = []
for i in range(1, len(uvxy)):
    uvxy_daily_percentage.append(round((uvxy[i]-uvxy[i-1])/uvxy[i-1]+1, 6))
print(uvxy_daily_percentage[:10])
# uvxy_daily_percentage = pd.DataFrame(uvxy_daily_percentage, columns=['ratio'])


# type(uvxy)
tmp = total_asset[0]
for ratio in uvxy_daily_percentage:
    tmp = round(tmp*ratio, 1)
    total_asset.append(tmp)
# total_asset = total_asset[:10]
# print(total_asset)
total_asset = pd.DataFrame(total_asset, columns=['Close'])
# print(total_asset)


# import plotly.graph_objects as go
fig = go.Figure(data=[go.Scatter(x=qqq['Date'][1:],
                                 #  open=qqq['Open'],
                                 #  high=qqq['High'],
                                 #  low=qqq['Low'],
                                 y=total_asset['Close'],
                                 )])
# fig = go.Figure(data=[go.Candlestick(x=qqq['Date'][1:],
#                                      #  open=qqq['Open'],
#                                      #  high=qqq['High'],
#                                      #  low=qqq['Low'],
#                                      close=total_asset['Close'],
#                                      )]).update_layout(title_font_size=24)

# fig.update_layout(xaxis_rangeslider_visible=False, yaxis_type="log")
fig.show()
