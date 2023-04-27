# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 20:27:42 2022


@author: PIJHUSH

https://towardsdatascience.com/the-easiest-way-to-pull-stock-data-into-your-python-program-yfinance-82c304ae35dc

"""

import yfinance as yf
import pendulum
import matplotlib.pyplot as plt



price_history = yf.Ticker('TSLA').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
time_series = list(price_history['Open'])
dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]
plt.style.use('dark_background')
plt.plot(dt_list, time_series, linewidth=2)



price_history1 = yf.Ticker('TSLA').history(period='1d', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1m', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
time_series = list(price_history1['Open'])
dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]
plt.style.use('dark_background')
plt.plot(dt_list, time_series, linewidth=2)


################################################################################
# History data need to be checked daily.

# One day data, interval used 1 minuts
price_history2 = yf.Ticker('CVNA').history(period='1d', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1m', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)


# cd C:\Users\PIJHUSH\Desktop\Python with Spyder\Shear
price_history2.to_csv("./Todats_data.csv")


# 5 days, interval used 1 minuts
price_history3 = yf.Ticker('CVNA').history(period='5d', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                           interval='1m', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                           actions=False)

# cd C:\Users\PIJHUSH\Desktop\Python with Spyder\Shear
price_history2.to_csv("./Todats_data1.csv")



# One month data, interval used 1 minuts
price_history3 = yf.Ticker('CVNA').history(period='1mo', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                           interval='5m', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                           actions=False)

# cd C:\Users\PIJHUSH\Desktop\Python with Spyder\Shear
price_history2.to_csv("./Todats_data1.csv")





################################################################################
#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

import yfinance as yf

#define the ticker symbol
tickerSymbol = 'CVNA'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2022-11-16', end='2022-11-16')

# Current date 1 min interval
tickerDf = tickerData.history(period='1d', interval='1m', actions=False )
#see your data
tickerDf


# Plot
time_series = list(tickerDf['Open'])

dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(tickerDf.index)]
plt.style.use('dark_background')
plt.plot(dt_list, time_series, linewidth=2)



################################################################################
#Predicting Stock Prices with Python
#https://towardsdatascience.com/predicting-stock-prices-with-python-ec1d0c9bece1

#Downloading historical stock prices in Python
#https://towardsdatascience.com/downloading-historical-stock-prices-in-python-93f85f059c1f



######################################################################################

import finplot as fplt
import yfinance
df = yfinance.download('AAPL')
fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
fplt.show()

