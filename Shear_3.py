# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 23:34:51 2022

@author: PIJHUSH
"""

import yfinance as yf


company = 'CVNA'
company = 'SMMT'
# History data need to be checked daily.
# One day data, interval used 1 minuts
Ph_1d1m = yf.Ticker(company).history(period='1d', interval='1m', actions=False)
Ph_5d1m = yf.Ticker(company).history(period='5d', interval='1m', actions=False)
Ph_10d5m = yf.Ticker(company).history(period='10d', interval='5m', actions=False)
Ph_15d5m = yf.Ticker(company).history(period='15d', interval='5m', actions=False)
Ph_20d5m = yf.Ticker(company).history(period='20d', interval='5m', actions=False)
Ph_25d5m = yf.Ticker(company).history(period='25d', interval='5m', actions=False)
Ph_30d5m = yf.Ticker(company).history(period='30d', interval='5m', actions=False)
Ph_60d5m = yf.Ticker(company).history(period='60d', interval='5m', actions=False)


#Date wise 
Ph_1d1m = yf.Ticker(company).history(period='1d', 
                                     start='2022-11-30', 
                                     end='2022-12-1', 
                                     interval='1m', 
                                     actions=False)
Ph_1d1m = yf.Ticker(company).history(period='1d', start='2022-12-1', interval='1m', actions=False)



# cd C:\Users\PIJHUSH\Desktop\Python with Spyder\Shear
Ph_1d1m.to_csv("./Ph_1d1m_"+company+".csv")
Ph_5d1m.to_csv("./Ph_5d1m_"+company+".csv")
Ph_10d5m.to_csv("./Ph_10d5m_"+company+".csv")
Ph_15d5m.to_csv("./Ph_15d5m_"+company+".csv")
Ph_20d5m.to_csv("./Ph_20d5m_"+company+".csv")
Ph_25d5m.to_csv("./Ph_25d5m_"+company+".csv")
Ph_30d5m.to_csv("./Ph_30d5m_"+company+".csv")
Ph_60d5m.to_csv("./Ph_60d5m_"+company+".csv")



