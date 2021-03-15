
import matplotlib.pyplot as pp

# company which has date, Close


def mdd(company,  title=''):
    Roll_Max = company['Close'].cummax()
    Daily_Drawdown = company['Close']/Roll_Max - 1.0
    # Daily_Drawdown
    Max_Daily_Drawdown = Daily_Drawdown.cummin()

    window = 252

    # Calculate the max drawdown in the past window days for each day in the series.
    # Use min_periods=1 if you want to let the first 252 days data have an expanding window
    Roll_Max = company['Close'].rolling(window, min_periods=1).max()
    Daily_Drawdown = company['Close']/Roll_Max - 1.0

    # Next we calculate the minimum (negative) daily drawdown in that window.
    # Again, use min_periods=1 if you want to allow the expanding window
    Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()
    Max_Daily_Drawdown
    # Plot the results
    Daily_Drawdown.plot()
    Max_Daily_Drawdown.plot()
    # pp.title('TQQQ UVXY 8:2 MDD: {}%'.format(
    #     round(min(Max_Daily_Drawdown)*100, 2)))
    # if title != '':
    #     print("title !=''")
    #     pp.title('{} MDD: {}%'.format(title,
    #                                   round(min(Max_Daily_Drawdown)*100, 2)))
    # else:
    # print(x_data)
    # fig, ax = plt.subplots()
    # ax.xticks(x_data)
    pp.title('{} MDD: {}%'.format(title,
                                  round(min(Max_Daily_Drawdown)*100, 2)))

    pp.show()
    print('MDD:', round(min(Max_Daily_Drawdown)*100, 2), '%')
    return round(min(Max_Daily_Drawdown)*100, 2)
