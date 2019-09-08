import pandas as pd
from datetime import datetime
import numpy as np  
import  os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

selection = ['ALAQAR','TM','SAPNRG','VITROX','RANHILL']

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','dataset')

in_dir = parser.get('directory','company_stock_marketprice_baseprice_raw')



df_input =pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+selection[3]+'.csv')
date_query =  df_input['date'] >= '2010-03-25'

df = pd.DataFrame({ 
                    'date' : df_input['date'][date_query],
                    'open':df_input['open'][date_query],
                    'high':df_input['high'][date_query],
                    'low':df_input['low'][date_query],
                    'close':df_input['close'][date_query],
                    'volume':df_input['volume'][date_query]

                    })

df.to_csv(current_dir+"/"+base_dir+"/"+selection[3]+'_ml.csv',index=False)