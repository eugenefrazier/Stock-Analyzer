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
    #####  Momentum Indicator Functions #####
    #########################################



    #ADX - Average Directional Movement Index
    adx = ta.ADX(high, low, close, timeperiod=14)

    #ADXR - Average Directional Movement Index Rating
    adxr = ta.ADXR(high, low, close, timeperiod=14)

    #APO - Absolute Price Oscillator
    apo = ta.APO(close, fastperiod=12, slowperiod=26, matype=0)

    #AROON - Aroon
    aroondown, aroonup = ta.AROON(high, low, timeperiod=14)

    #AROONOSC - Aroon Oscillator
    aroonosc = ta.AROONOSC(high, low, timeperiod=14)

    #BOP - Balance Of Power
    bop = ta.BOP(openp, high, low, close)

    #CCI - Commodity Channel Index
    cci = ta.CCI(high, low, close, timeperiod=14)

    #CMO - Chande Momentum Oscillator
    cmo = ta.CMO(close, timeperiod=14)

    #DX - Directional Movement Index
    dx = ta.DX(high, low, close, timeperiod=14)

    #MACD - Moving Average Convergence/Divergence
    macd, macdsignal, macdhist = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

    #MACDEXT - MACD with controllable MA type
    macd, macdsignal, macdhist = ta.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)

    #MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    macd, macdsignal, macdhist = ta.MACDFIX(close, signalperiod=9)

    #MFI - Money Flow Index
    mfi = ta.MFI(high, low, close, volume, timeperiod=14)

    #MINUS_DI - Minus Directional Indicator
    minus_di = ta.MINUS_DI(high, low, close, timeperiod=14)

    #MINUS_DM - Minus Directional Movement
    minus_dm = ta.MINUS_DM(high, low, timeperiod=14)

    #MOM - Momentum
    mom = ta.MOM(close, timeperiod=10)

    #PLUS_DI - Plus Directional Indicator
    plus_di = ta.PLUS_DI(high, low, close, timeperiod=14)

    #PLUS_DM - Plus Directional Movement
    plus_dm = ta.PLUS_DM(high, low, timeperiod=14)

    #PPO - Percentage Price Oscillator
    ppo = ta.PPO(close, fastperiod=12, slowperiod=26, matype=0)

    #ROC - Rate of change : ((price/prevPrice)-1)*100
    roc = ta.ROC(close, timeperiod=10)

    #ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    rocp = ta.ROCP(close, timeperiod=10)

    #ROCR - Rate of change ratio: (price/prevPrice)
    rocr = ta.ROCR(close, timeperiod=10)

    #ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    rocr100 = ta.ROCR100(close, timeperiod=10)

    #RSI - Relative Strength Index
    rsi = ta.RSI(close, timeperiod=14)

    #STOCH - Stochastic
    slowk, slowd = ta.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

    #STOCHF - Stochastic Fast
    stochf_fastk, stochf_fastd = ta.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)

    #STOCHRSI - Stochastic Relative Strength Index
    stochrsi_fastk, stochrsi_fastd = ta.STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)

    #TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    trix = ta.TRIX(close, timeperiod=30)

    #ULTOSC - Ultimate Oscillator
    ultosc = ta.ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)

    #WILLR - Williams' %R
    willr = ta.WILLR(high, low, close, timeperiod=14)

    df_save = pd.DataFrame(data ={
        'Date': np.array(df['date']),
        'adx':adx,
        'adxr':adxr,
        'apo':apo,
        'aroondown':aroondown,
        'aroonup' : aroonup ,
        'aroonosc':aroonosc,
        'bop':bop,
        'cci':cci,
        'cmo':cmo,
        'dx':dx,
        'macd':macd, 
        'macdsignal':macdsignal, 
        'macdhist':macdhist,
        'mfi':mfi,
        'minus_di':minus_di,
        'minus_dm':minus_dm,
        'mom':mom,
        'plus_di':plus_di,
        'plus_dm':plus_dm,
        'ppo':ppo,
        'roc':roc,
        'rocp':rocp,
        'rocr':rocr,
        'rocr100':rocr100,
        'rsi':rsi,
        'slowk':slowk,
        'slowd':slowd,
        'stochf_fastk':stochf_fastk, 
        'stochf_fastd':stochf_fastd,
        'stochrsi_fastk':stochrsi_fastk,
        'stochrsi_fastd':stochrsi_fastd,
        'trix':trix,
        'ultosc':ultosc,
        'willr':willr
    })

    df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_ta_momentum_indicator_'+stock_symbol+'.csv',index=False)

if __name__ == '__main__':
    main()