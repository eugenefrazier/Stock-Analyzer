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
    ##### Pattern Recognition Functions #####
    #########################################




    #CDL2CROWS - Two Crows
    cdl2crows = ta.CDL2CROWS(openp, high, low, close)

    #CDL3BLACKCROWS - Three Black Crows
    cdl3blackcrows = ta.CDL3BLACKCROWS(openp, high, low, close)

    #CDL3INSIDE - Three Inside Up/Down
    cdl3inside = ta.CDL3INSIDE(openp, high, low, close)

    #CDL3LINESTRIKE - Three-Line Strike
    cdl3linestrike = ta.CDL3LINESTRIKE(openp, high, low, close)

    #CDL3OUTSIDE - Three Outside Up/Down
    cdl3outside = ta.CDL3OUTSIDE(openp, high, low, close)

    #CDL3STARSINSOUTH - Three Stars In The South
    cdl3starinsouth = ta.CDL3STARSINSOUTH(openp, high, low, close)

    #CDL3WHITESOLDIERS - Three Advancing White Soldiers
    cdl3whitesoldiers = ta.CDL3WHITESOLDIERS(openp, high, low, close)

    #CDLABANDONEDBABY - Abandoned Baby
    cdlabandonbaby = ta.CDLABANDONEDBABY(openp, high, low, close, penetration=0)

    #CDLADVANCEBLOCK - Advance Block
    cdladvanceblock = ta.CDLADVANCEBLOCK(openp, high, low, close)

    #CDLBELTHOLD - Belt-hold
    cdlbelthold = ta.CDLBELTHOLD(openp, high, low, close)

    #CDLBREAKAWAY - Breakaway
    cdlbreakway = ta.CDLBREAKAWAY(openp, high, low, close)

    #CDLCLOSINGMARUBOZU - Closing Marubozu
    cdlclosingmarubozu = ta.CDLCLOSINGMARUBOZU(openp, high, low, close)

    #CDLCONCEALBABYSWALL - Concealing Baby Swallow
    cdlconcealbabyswall = ta.CDLCONCEALBABYSWALL(openp, high, low, close)

    #CDLCOUNTERATTACK - Counterattack
    cdlcounterattack = ta.CDLCOUNTERATTACK(openp, high, low, close)

    #CDLDARKCLOUDCOVER - Dark Cloud Cover
    cdldarkcloudcover = ta.CDLDARKCLOUDCOVER(openp, high, low, close, penetration=0)

    #CDLDOJI - Doji
    cdldoji = ta.CDLDOJI(openp, high, low, close)

    #CDLDOJISTAR - Doji Star
    cdldojistar = ta.CDLDOJISTAR(openp, high, low, close)

    #CDLDRAGONFLYDOJI - Dragonfly Doji
    cdldragonflydoji = ta.CDLDRAGONFLYDOJI(openp, high, low, close)

    #CDLENGULFING - Engulfing Pattern
    cdlengulfing = ta.CDLENGULFING(openp, high, low, close)

    #CDLEVENINGDOJISTAR - Evening Doji Star
    cdeveningdojistar = ta.CDLEVENINGDOJISTAR(openp, high, low, close, penetration=0)

    #CDLEVENINGSTAR - Evening Star
    cdeveningstar = ta.CDLEVENINGSTAR(openp, high, low, close, penetration=0)

    #CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    cdlgapsidesidewhite = ta.CDLGAPSIDESIDEWHITE(openp, high, low, close)

    #CDLGRAVESTONEDOJI - Gravestone Doji
    cdlgravestonedoji = ta.CDLGRAVESTONEDOJI(openp, high, low, close)

    #CDLHAMMER - Hammer
    cdlhammer = ta.CDLHAMMER(openp, high, low, close)

    #CDLHANGINGMAN - Hanging Man
    cdlhangman = ta.CDLHANGINGMAN(openp, high, low, close)

    #CDLHARAMI - Harami Pattern
    cdlharami = ta.CDLHARAMI(openp, high, low, close)

    #CDLHARAMICROSS - Harami Cross Pattern
    cdlharamicross = ta.CDLHARAMICROSS(openp, high, low, close)

    #CDLHIGHWAVE - High-Wave Candle
    cdlhighwave = ta.CDLHIGHWAVE(openp, high, low, close)

    #CDLHIKKAKE - Hikkake Pattern
    cdlhikakke = ta.CDLHIKKAKE(openp, high, low, close)

    #CDLHIKKAKEMOD - Modified Hikkake Pattern
    cdlhikkakemod = ta.CDLHIKKAKEMOD(openp, high, low, close)

    #CDLHOMINGPIGEON - Homing Pigeon
    cdlhomingpigeon = ta.CDLHOMINGPIGEON(openp, high, low, close)

    #CDLIDENTICAL3CROWS - Identical Three Crows
    cdlidentical3crows = ta.CDLIDENTICAL3CROWS(openp, high, low, close)

    #CDLINNECK - In-Neck Pattern
    cdlinneck = ta.CDLINNECK(openp, high, low, close)

    #CDLINVERTEDHAMMER - Inverted Hammer
    cdlinvertedhammer = ta.CDLINVERTEDHAMMER(openp, high, low, close)

    #CDLKICKING - Kicking
    cdkicking = ta.CDLKICKING(openp, high, low, close)

    #CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    cdkickingbylength = ta.CDLKICKINGBYLENGTH(openp, high, low, close)

    #CDLLADDERBOTTOM - Ladder Bottom
    cdlladderbottom = ta.CDLLADDERBOTTOM(openp, high, low, close)

    #CDLLONGLEGGEDDOJI - Long Legged Doji
    cdllongleggeddoji = ta.CDLLONGLEGGEDDOJI(openp, high, low, close)

    #CDLLONGLINE - Long Line Candle
    cdllongline = ta.CDLLONGLINE(openp, high, low, close)

    #CDLMARUBOZU - Marubozu
    cdlmarubozu = ta.CDLMARUBOZU(openp, high, low, close)

    #CDLMATCHINGLOW - Matching Low
    cdlmatchinglow = ta.CDLMATCHINGLOW(openp, high, low, close)

    #CDLMATHOLD - Mat Hold
    cdlmathold = ta.CDLMATHOLD(openp, high, low, close, penetration=0)

    #CDLMORNINGDOJISTAR - Morning Doji Star
    cdlmorningdojistar = ta.CDLMORNINGDOJISTAR(openp, high, low, close, penetration=0)

    #CDLMORNINGSTAR - Morning Star
    cdlmorningstar = ta.CDLMORNINGSTAR(openp, high, low, close, penetration=0)

    #CDLONNECK - On-Neck Pattern
    cdlonneck = ta.CDLONNECK(openp, high, low, close)

    #CDLPIERCING - Piercing Pattern
    cdlpiercing = ta.CDLPIERCING(openp, high, low, close)

    #CDLRICKSHAWMAN - Rickshaw Man
    cdlrickshawman = ta.CDLRICKSHAWMAN(openp, high, low, close)

    #CDLRISEFALL3METHODS - Rising/Falling Three Methods
    cdlrisefall3methods = ta.CDLRISEFALL3METHODS(openp, high, low, close)

    #CDLSEPARATINGLINES - Separating Lines
    cdlseperatinglines = ta.CDLSEPARATINGLINES(openp, high, low, close)

    #CDLSHOOTINGSTAR - Shooting Star
    cdlshootingstar = ta.CDLSHOOTINGSTAR(openp, high, low, close)

    #CDLSHORTLINE - Short Line Candle
    cdlshortline = ta.CDLSHORTLINE(openp, high, low, close)

    #CDLSPINNINGTOP - Spinning Top
    cdlspinningtop = ta.CDLSPINNINGTOP(openp, high, low, close)

    #CDLSTALLEDPATTERN - Stalled Pattern
    cdlstalledpattern = ta.CDLSTALLEDPATTERN(openp, high, low, close)

    #CDLSTICKSANDWICH - Stick Sandwich
    cdlsticksandwich = ta.CDLSTICKSANDWICH(openp, high, low, close)

    #CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
    cdltakuri = ta.CDLTAKURI(openp, high, low, close)

    #CDLTASUKIGAP - Tasuki Gap
    cdltasukigap = ta.CDLTASUKIGAP(openp, high, low, close)

    #CDLTHRUSTING - Thrusting Pattern
    cdlthrusting = ta.CDLTHRUSTING(openp, high, low, close)

    #CDLTRISTAR - Tristar Pattern
    cdltristar = ta.CDLTRISTAR(openp, high, low, close)

    #CDLUNIQUE3RIVER - Unique 3 River
    cdlunique3river = ta.CDLUNIQUE3RIVER(openp, high, low, close)

    #CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    cdlupsidegap2crows = ta.CDLUPSIDEGAP2CROWS(openp, high, low, close)

    #CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    cdlxsidegap3methods = ta.CDLXSIDEGAP3METHODS(openp, high, low, close)



    df_save = pd.DataFrame(data ={

        'date': np.array(df['date']),
        'cdl2crows':    cdl2crows, 
        'cdl3blackcrows': cdl3blackcrows, 
        'cdl3inside':cdl3inside,
        'cdl3linestrike':  cdl3linestrike, 
        'cdl3outside' :cdl3outside, 
        'cdl3starinsouth' :cdl3starinsouth,
        'cdl3whitesoldiers':cdl3whitesoldiers,
        'cdlabandonbaby' :cdlabandonbaby,
        'cdladvanceblock' : cdladvanceblock,
        'cdlbelthold': cdlbelthold,
        'cdlbreakway' : cdlbreakway, 
        'cdlclosingmarubozu' : cdlclosingmarubozu, 
        'cdlconcealbabyswall' :cdlconcealbabyswall,
        'cdlcounterattack' : cdlcounterattack,
        'cdldarkcloudcover' : cdldarkcloudcover,
        'cdldoji' : cdldoji,
        'cdldojistar' :cdldojistar, 
        'cdldragonflydoji' : cdldragonflydoji,
        'cdlengulfing' : cdlengulfing, 
        'cdeveningdojistar' : cdeveningdojistar,
        'cdeveningstar' : cdeveningstar, 
        'cdlgapsidesidewhite' : cdlgapsidesidewhite,
        'cdlgravestonedoji' : cdlgravestonedoji,
        'cdlhammer' :cdlhammer,
        'cdlhangman' : cdlhangman, 
        'cdlharami' :cdlharami, 
        'cdlharamicross' : cdlharamicross,
        'cdlhighwave' : cdlhighwave,
        'cdlhikakke' : cdlhikakke, 
        'cdlhikkakemod' : cdlhikkakemod, 
        'cdlhomingpigeon' : cdlhomingpigeon, 
        'cdlidentical3crows' : cdlidentical3crows,
        'cdlinneck' : cdlinneck, 
        'cdlinvertedhammer' :cdlinvertedhammer, 
        'cdkicking' : cdkicking, 
        'cdkickingbylength' : cdkickingbylength, 
        'cdlladderbottom' :cdlladderbottom, 
        'cdllongleggeddoji' : cdllongleggeddoji, 
        'cdllongline' : cdllongline, 
        'cdlmarubozu' : cdlmarubozu,
        'cdlmatchinglow' : cdlmatchinglow,
        'cdlmathold' : cdlmathold,
        'cdlmorningdojistar' : cdlmorningdojistar,
        'cdlmorningstar' : cdlmorningstar, 
        'cdlonneck' : cdlonneck,
        'cdlpiercing' : cdlpiercing,
        'cdlrickshawman' : cdlrickshawman,
        'cdlrisefall3methods' : cdlrisefall3methods, 
        'cdlseperatinglines' : cdlseperatinglines,
        'cdlshootingstar' : cdlshootingstar, 
        'cdlshortline' : cdlshortline, 
        'cdlspinningtop' : cdlspinningtop, 
        'cdlstalledpattern' : cdlstalledpattern, 
        'cdlsticksandwich' : cdlsticksandwich, 
        'cdltakuri' : cdltakuri, 
        'cdltasukigap' : cdltasukigap, 
        'cdlthrusting' : cdlthrusting,
        'cdltristar' : cdltristar, 
        'cdlunique3river' : cdlunique3river, 
        'cdlupsidegap2crows' : cdlupsidegap2crows,
        'cdlxsidegap3methods' : cdlxsidegap3methods 
    })

    df_save.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_ta_pattern_reognition_'+stock_symbol+'.csv',index=False)

if __name__ == '__main__':
    main()