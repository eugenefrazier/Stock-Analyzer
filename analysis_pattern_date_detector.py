import pandas as pd
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))


base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_processed')


current_dir = os.path.dirname(os.path.realpath(__file__))



while True:
        stock_symbol = input("Type a stock to analyse (refer to pattern list , eg : CIMB) : ")
        ta_pattern = input("Type a pattern to analyse (refer to pattern list , eg : cdlmarubozu) : ")

        try:
                df = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+stock_symbol+"/"+in_dir+'_ta_pattern_recognition_'+stock_symbol+'.csv')

                for i in range(0,df[ta_pattern].count()): 
                        if(df[ta_pattern][i]!=0):
                                print(stock_symbol+" "+ta_pattern+' pattern detected at '+df['date'][i])
        
        except:
                print("Error Restarting")
