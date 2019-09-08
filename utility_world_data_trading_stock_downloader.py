import pandas as pd
from pandas.io.json import json_normalize
import os
from datetime import datetime
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_datalist_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_baseprice_raw')

class worldtradedata():

    def __init__(self):

        self.country = parser.get('world_trade_data_settings','country')
        self.api_token = parser.get('world_trade_data_settings','api_token')
        self.web_base = parser.get('world_trade_data_settings','web_base')
        self.webAPI = parser.get('world_trade_data_settings','webAPI')

    def historical_market_data(self):

        print('[Comment]Downloading data from http://worldtradingdata.com/ ')
        syms =[e.strip() for e in parser.get('general_settings','syms').split(',')]

        for sym in range(0,len(syms)):
            #dont forget to put debugging
            comp_datalist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+syms[sym]+".csv",dtype =str)

            
            for i in range(0,comp_datalist['stock_code'].count()):

                try:

                    print('['+str(i)+'] Downloading '+str(comp_datalist['stock_symbol'][i]))

                    full_url = self.web_base+comp_datalist['stock_code'][i]+"."+self.country+self.webAPI+self.api_token
                    data = pd.read_json(full_url)
                    df = json_normalize(data['history'])

                    data_new = pd.DataFrame({
                        
                        'date':data.index,
                        'open':df['open'].astype('float'),
                        'close':df['close'].astype('float'),
                        'high':df['high'].astype('float'),
                        'low':df['low'].astype('float'),
                        'volume':df['volume']
                    })
                    
                    data_new.to_csv(current_dir+"/"+base_dir+"/"+out_dir+"/"+out_dir+"_"+comp_datalist['stock_symbol'][i]+".csv",index=False)
                    print('[Status]'+str(comp_datalist['stock_symbol'][i])+" has been downloaded successfully")

                except:

                    print('['+str(i)+'] Error '+str(comp_datalist['stock_symbol'][i])+" failed to download")

if __name__ == "__main__":
    worldtradedata().historical_market_data()

    