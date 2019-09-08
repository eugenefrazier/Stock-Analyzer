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

        print("[Status]Processing TA Math Transform for "+comp_datalist['stock_symbol'][i])

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
        #####  Math Transform Functions ######
        #########################################
        
        #ACOS - Vector Trigonometric ACos
        acos = ta.ACOS(close)

        #ASIN - Vector Trigonometric ASin
        asin = ta.ASIN(close)

        #ATAN - Vector Trigonometric ATan
        atan = ta.ATAN(close)

        #CEIL - Vector Ceil
        ceil = ta.CEIL(close)

        #COS - Vector Trigonometric Cos
        cos = ta.COS(close)

        #COSH - Vector Trigonometric Cosh
        cosh = ta.COSH(close)

        #EXP - Vector Arithmetic Exp
        exp = ta.EXP(close)

        #FLOOR - Vector Floor
        floor = ta.FLOOR(close)

        #LN - Vector Log Natural
        ln = ta.LN(close)

        #LOG10 - Vector Log10
        log10 = ta.LOG10(close)

        #SIN - Vector Trigonometric Sin
        sin = ta.SIN(close)

        #SINH - Vector Trigonometric Sinh
        sinh = ta.SINH(close)

        #SQRT - Vector Square Root
        sqrt = ta.SQRT(close)

        #TAN - Vector Trigonometric Tan
        tan = ta.TAN(close)

        #TANH - Vector Trigonometric Tanh
        tanh = ta.TANH(close)


        df_save = pd.DataFrame(data ={
            'date': np.array(df['date']),
            'acos':acos,
            'asin':asin,
            'atan':atan,
            'ceil':ceil,
            'cos':cos,
            'cosh':cosh,
            'exp':exp,
            'floor':floor,
            'ln':ln,
            'log10':log10,
            'sin':sin,
            'sinh':sinh,
            'sqrt':sqrt,
            'tan':tan,
            'tanh':tanh

        })

        df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_ta_math_transform_'+comp_datalist['stock_symbol'][i]+'.csv',index=False)

    except:
        print("[Status]Error fail to processed TA Math Transform for "+comp_datalist['stock_symbol'][i])

        