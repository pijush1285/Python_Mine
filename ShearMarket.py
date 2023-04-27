# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:39:11 2022

@author: PIJHUSH
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

start = dt.datetime(2022, 11, 12)
end = dt.datetime.now()

df = web.DataReader("CVNA", 'yahoo', start, end)
print(df.head())



import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web



df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())



style.use('ggplot')

start = dt.datetime(2022, 9, 2)
end = dt.datetime.now()
df = web.DataReader("META", 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())

df.plot()
plt.show()
