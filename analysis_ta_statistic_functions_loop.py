import numpy as np
import pandas as pd
import talib as ta
from talib import MA_Type
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_datalist_prefilter')
in_dir1 = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

comp_datalist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_combined.csv")

for i in range(0,comp_datalist['stock_symbol'].count()):
    try:

        # read csv file and transform it to datafeed (df):
        df = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir1+"/"+in_dir1+'_'+comp_datalist['stock_symbol'][i]+'.csv')

        print("[Status]Processing TA Statistic Functions for "+comp_datalist['stock_symbol'][i])

        # set numpy datafeed from df:
        df_numpy = {
            'Date': np.array(df['date']),
            'Open': np.array(df['open'], dtype='float'),
            'High': np.array(df['high'], dtype='float'),
            'Low': np.array(df['low'], dtype='float'),
            'Close': np.array(df['close'], dtype='float'),
            'Volume': np.array(df['volume'], dtype='float')
            }

        date = df_numpy['Date']
        openp = df_numpy['Open']
        high = df_numpy['High']
        low = df_numpy['Low']
        close = df_numpy['Close']
        volume = df_numpy['Volume']



        #########################################
        ########## Statistic Function ###########
        #########################################



        #BETA - Beta of 5
        beta = ta.BETA(high, low, timeperiod=5)

        #CORREL - Pearson's Correlation Coefficient (r)
        correl = ta.CORREL(high, low, timeperiod=30)

        #LINEARREG - Linear Regression
        linearreg = ta.LINEARREG(close, timeperiod=14)

        #LINEARREG_ANGLE - Linear Regression Angle
        linearreg_angle = ta.LINEARREG_ANGLE(close, timeperiod=14)

        #LINEARREG_INTERCEPT - Linear Regression Intercept
        linearreg_intercept = ta.LINEARREG_INTERCEPT(close, timeperiod=14)

        #LINEARREG_SLOPE - Linear Regression Slope
        linearreg_slope = ta.LINEARREG_SLOPE(close, timeperiod=14)

        #STDDEV - Standard Deviation
        stdev = ta.STDDEV(close, timeperiod=5, nbdev=1)

        #TSF - Time Series Forecast
        tsf = ta.TSF(close, timeperiod=14)

        #VAR - Variance 
        var = ta.VAR(close, timeperiod=5, nbdev=1)



        df_save = pd.DataFrame(data ={
            'date': np.array(df['date']),
            'beta': beta,
            'correl':correl,
            'linearreg':linearreg,
            'linearreg':linearreg_angle,
            'linearreg_intercept':linearreg_intercept,
            'linearreg_slope':linearreg_slope,
            'stdev':stdev,
            'tsf':tsf,
            'var':var

        })


        df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_ta_statistic_functions_'+comp_datalist['stock_symbol'][i]+'.csv',index=False)

    except:
        print("[Status]Error fail to processed TA Statistic Functions for "+comp_datalist['stock_symbol'][i])