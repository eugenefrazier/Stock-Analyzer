import numpy as np
import pandas as pd
import talib as ta
from talib import MA_Type
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

stock_symbol = parser.get('analysis','stock_symbol')
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

def main():
    # read csv file and transform it to datafeed (df):
    df = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+stock_symbol+'.csv')

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
    #####  Price Transform Functions #####
    #########################################



    #AVGPRICE - Average Price
    avgprice = ta.AVGPRICE(openp, high, low, close)

    #MEDPRICE - Median Price
    medprice = ta.MEDPRICE(high, low)

    #TYPPRICE - Typical Price
    typprice = ta.TYPPRICE(high, low, close)

    #WCLPRICE - Weighted Close Price
    wclprice = ta.WCLPRICE(high, low, close)


    df_save = pd.DataFrame(data ={
        'date': np.array(df['date']),
        'avgprice':avgprice,
        'medprice':medprice,
        'typprice':typprice,
        'wclprice':wclprice
    })

    df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_ta_price_transform_'+stock_symbol+'.csv',index=False)

if __name__ == '__main__':
    main()