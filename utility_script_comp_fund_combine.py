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
in_dir = parser.get('directory','company_fund_marketprice_prefilter')
out_dir  = parser.get('directory','debug_file')

df_out = []

syms =[e.strip() for e in parser.get('general_settings','syms').split(',')]

for sym in range(0,len(syms)):

    df_input =pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+current_date+"/"+in_dir+"_"+current_date+"_"+syms[sym]+'.csv')

    df = pd.DataFrame({ 
        
        'stock_symbol': df_input['stock_symbol'],
        'mcap': df_input['mcap'],
        'num_of_share':df_input['num_of_share'],
        'eps':df_input['eps'],
        'pe_ratio':df_input['pe_ratio'],
        'roe':df_input['roe'],
        'div':df_input['div'],
        'div_y':df_input['div_y'],
        'div_p':df_input['div_p'],
        'nta':df_input['nta'],
        'par_v':df_input['par_v'] })

    df_out.append(df)

df_out = pd.concat(df_out)
df_out.to_csv(current_dir+"/"+base_dir+"/"+out_dir+"/"+out_dir+'_'+in_dir+'_combined_'+current_year+'.csv',index=False)