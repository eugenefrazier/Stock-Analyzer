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

        print("[Status]Processing TA Math Operator for "+comp_datalist['stock_symbol'][i])
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
        #####  Math Operator Functions ######
        #########################################

        #ADD - Vector Arithmetic Add
        add = ta.ADD(high, low)

        #DIV - Vector Arithmetic Div
        div = ta.DIV(high, low)

        #MAX - Highest value over a specified period
        maxv = ta.MAX(close, timeperiod=30)

        #MAXINDEX - Index of highest value over a specified period
        maxindex = ta.MAXINDEX(close, timeperiod=30)

        #MIN - Lowest value over a specified period
        minv = ta.MIN(close, timeperiod=30)

        #MININDEX - Index of lowest value over a specified period
        minindex = ta.MININDEX(close, timeperiod=30)

        #MINMAX - Lowest and highest values over a specified period
        minsp, maxsp = ta.MINMAX(close, timeperiod=30)

        #MINMAXINDEX - Indexes of lowest and highest values over a specified period
        minidx, maxidx = ta.MINMAXINDEX(close, timeperiod=30)

        #MULT - Vector Arithmetic Mult
        mult = ta.MULT(high, low)

        #SUB - Vector Arithmetic Substraction
        sub = ta.SUB(high, low)

        #SUM - Summation
        sum = ta.SUM(close, timeperiod=30)



        df_save = pd.DataFrame(data ={
        'date': np.array(df['date']),
        'add': add,
        'div':div,
        'max':maxv,
        'maxindex':maxindex,
        'min':minv,
        'minindex' : minindex,
        'min_spec_period':minsp,
        'max_spec_period':maxsp,
        'minidx':minidx,
        'maxidx':maxidx,
        'mult':mult,
        'sub':sub,
        'sum':sum
        })

        df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_ta_math_operator_'+comp_datalist['stock_symbol'][i]+'.csv',index=False)
    
    except:

        print("[Status]Error fail to processed TA Math Operator for "+comp_datalist['stock_symbol'][i])