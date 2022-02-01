import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.lines as mlines

# Run with  $ python view.py [CSV DATA NAME].csv [results].csv
# example: python view.py Binance_LINKUSDT_d.csv

df = pd.read_csv(str(sys.argv[1]), skiprows=1)
close = df.iloc[:, 6].tolist()
close.reverse() #reverse bc csv data is from present to past order
dates = df.iloc[:, 1].tolist()
dates.reverse()
# print(len(close))

period = 35
intervals = np.ceil(len(close)/period)
# print(intervals)

sum = 0
terms = 0
moving_avg = []
period_dates = []
for i in range(len(close) - period,len(close)):
  # print(close[i], terms, moving_avg, dates[i][:10])
  sum += close[i]
  terms += 1
  moving_avg.append(sum/terms)
  period_dates.append(dates[i])

plt.plot(period_dates,close[len(close) - period:len(close)])
plt.plot(period_dates,moving_avg)
title = str(period) + " day Moving Average"
plt.title(title)
plt.show()
