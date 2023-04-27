# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:34:32 2022

@author: PIJHUSH
"""


import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'RNZPXZ6Q9FEFMEHM'



ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')

#You may also get a key from rapidAPI. Use your rapidAPI key for the key 
#variable, and set rapidapi=True
ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM',rapidapi=True)


# For the default date string index behavior
ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM',output_format='pandas', indexing_type='date')
# For the default integer index behavior
ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM',output_format='pandas', indexing_type='integer')


from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))


####################################################
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()

####################################################
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

ti = TechIndicators(key='RNZPXZ6Q9FEFMEHM', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()


####################################################
from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='RNZPXZ6Q9FEFMEHM', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()



####################################################
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

cc = CryptoCurrencies(key='RNZPXZ6Q9FEFMEHM', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()



