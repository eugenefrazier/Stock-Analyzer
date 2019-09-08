import pandas as pd
from datetime import datetime
import numpy as np  
import os
from datetime import datetime
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_year = datetime.now().strftime("%Y")
current_date = datetime.now().strftime("%y-%m-%d")
current_dir = os.path.dirname(os.path.realpath(__file__))

base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_datalist_prefilter')

df_out = []

syms =[e.strip() for e in parser.get('general_settings','syms').split(',')]


for sym in range(0,len(syms)):

    data =pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+syms[sym]+'.csv',dtype=str)

    df= pd.DataFrame({ 
        
        'company_name' : data['company_name'],
        'sector':  data['sector'],
        'stock_symbol': data['stock_symbol'].str.replace(" ",""),
        'stock_code' : data['stock_code'].str.replace(")","")})

    df_out.append(df)

df_out = pd.concat(df_out)
df_out.to_csv(current_dir+'/'+base_dir+'/'+in_dir+'/'+in_dir+'_combined.csv',index=False)