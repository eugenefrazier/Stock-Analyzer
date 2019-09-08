import pandas as pd
from datetime import datetime
import numpy as np  
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')

in_dir = parser.get('directory','company_stock_marketprice_baseprice_raw')
out_dir  = parser.get('directory','portfolio_dir')
portfolio_name = parser.get('portfolio_settings','portfolio_name')

selection = [e.strip() for e in parser.get('portfolio_settings','selection').split(',')]

df_out = []

for i in range(len(selection)):
    df_input =pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+selection[i]+'.csv')

    date_query  =  df_input['date'] >= parser.get('query','date_query')

    df = pd.DataFrame({ 
                        'date' : df_input['date'][date_query],
                        'ticker':selection[i],
                        'close':df_input['close'][date_query]
                        })
    df_out.append(df)

df_out = pd.concat(df_out)
try:
    os.mkdir(current_dir+"/"+base_dir+"/"+out_dir+'/'+portfolio_name) 
except:
    pass
    
df_out.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+portfolio_name+"/"+portfolio_name+"_selection.csv",index=False)