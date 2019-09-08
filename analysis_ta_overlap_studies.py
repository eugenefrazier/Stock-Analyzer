import numpy as np
import pandas as pd
import talib as ta
from talib import MA_Type
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

stock_symbol = parser.get('general_settings','stock_symbol')
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

def main():
    # read csv file and transform it to datafeed (df):
    df = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+stock_symbol+'.csv')

    # set numpy datafeed from df:
    df_numpy = {
        'date': np.array(df['date']),
        'open': np.array(df['open'], dtype='float'),
        'high': np.array(df['high'], dtype='float'),
        'low': np.array(df['low'], dtype='float'),
        'close': np.array(df['close'], dtype='float'),
        'volume': np.array(df['volume'], dtype='float')
        }

    date = df_numpy['date']
    openp = df_numpy['open']
    high = df_numpy['high']
    low = df_numpy['low']
    close = df_numpy['close']
    volume = df_numpy['volume']



    #########################################
    ####### Overlap Study Function ##########
    #########################################



    #Bollinger Band Indicator
    upperBB, middleBB, lowerBB = ta.BBANDS(close, matype=MA_Type.T3)

    #Double Exponential Moving Average
    dema = ta.DEMA(close, timeperiod=30)

    #Exponential Moving Average
    ema = ta.EMA(close, timeperiod=30)

    #HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    ht = ta.HT_TRENDLINE(close)

    #KAMA - Kaufman Adaptive Moving Average 
    kama = ta.KAMA(close, timeperiod=30)

    #MA10 - Moving average 10
    ma10 = ta.MA(close, timeperiod=10, matype=0)

    #MA100 - Moving average 
    ma100 = ta.MA(close, timeperiod=100, matype=0)

    #MAMA - MESA Adaptive Moving Average
    #mama, fama = ta.MAMA(close, fastlimit=0, slowlimit=0)

    #MAVP - Moving average with variable period
    #mavp = ta.MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)

    #MIDPOINT - MidPoint over period
    midpoint = ta.MIDPOINT(close, timeperiod=14)

    #MIDPRICE - Midpoint Price over period
    midprice = ta.MIDPRICE(high, low, timeperiod=14)

    #SAR - Parabolic SAR
    sar = ta.SAR(high, low, acceleration=0, maximum=0)

    #SAREXT - Parabolic SAR - Extended
    sarext = ta.SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)

    #Simple Moving Average indicator sample 10
    sma10 = ta.SMA(close, 10)

    #T3 - Triple Exponential Moving Average (T3)
    t3 = ta.T3(close, timeperiod=5, vfactor=0)

    #TEMA - Triple Exponential Moving Average
    tema = ta.TEMA(close, timeperiod=30)

    #TRIMA - Triangular Moving Average
    trima = ta.TRIMA(close, timeperiod=30)

    #WMA - Weighted Moving Average
    wma = ta.WMA(close, timeperiod=30)




    df_save = pd.DataFrame(data ={
        'date': date,
        'upperBB': upperBB,
        'middleBB':  middleBB, 
        'lowerBB':  lowerBB,
        'dema':dema,
        'ema':ema,
        'ht':ht,
        'kama':kama, 
        'ma10':ma10, 
        'ma100':ma100, 
        #'mama':mama, 
        #'fama':fama,
        'midpoint':midpoint, 
        'midprice':midprice,
        'sar':sar,
        'sarext':sarext, 
        'sma10':sma10,
        't3':t3,
        'tema':tema,
        'trima':trima, 
        'wma':wma,
        'close':close 
    })
    #df_save = df_save.dropna()
    df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_ta_overlap_studies_'+stock_symbol+'.csv',index=False)

if __name__ == '__main__':
    main()