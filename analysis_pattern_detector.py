################################################################################################
#	name:	timeseries_OHLC.py
#	desc:	creates OHLC graph
#	date:	2018-06-15
#	Author:	conquistadorjd
################################################################################################
import pandas as pd
# import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc

import matplotlib.dates as mdates
import os
import datetime
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

stock_symbol = parser.get('general_settings','stock_symbol')
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
in_dir1 = parser.get('directory','company_stock_marketprice_processed')
ta_pattern = parser.get('analysis','ta_pattern')

current_dir = os.path.dirname(os.path.realpath(__file__))

print('*** Program Started ***')

df = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+stock_symbol+'.csv')
ta = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir1+"/"+stock_symbol+"/"+in_dir1+'_ta_pattern_recognition_'+stock_symbol+'.csv')


dt = datetime.date(2004, 1, 26)
length = df['close'][df['date'] == str(dt)].values


signal ='cdlclosingmarubozu'
f1, ax = plt.subplots(figsize = (10,5))

# Converting date to pandas datetime format
df['date'] = pd.to_datetime(df['date'])
df["date"] = df["date"].apply(mdates.date2num)

for i in range(0,ta[signal].count()): 
    if(ta[signal][i]!=0):
        print("closing marubozou pattern detected at "+ta['date'][i])
        ax.annotate(signal, xy=(df['date'][i], length+0.05), xytext=(df['date'][i], length+0.5),
                    arrowprops=dict(facecolor='black'),
                )



# Creating required data in new DataFrame OHLC
ohlc= df[['date', 'open', 'high', 'low','close']].copy()

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.show()

print('*** Program ended ***')