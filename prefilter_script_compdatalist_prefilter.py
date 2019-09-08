# Pre-filtering needs improvement
import pandas as pd
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

dir_raw = parser.get('directory','company_datalist_raw')
dir_prefilter = parser.get('directory','company_datalist_prefilter')
base_file = parser.get('directory','base_dir')

syms = [e.strip() for e in parser.get('general_settings','syms').split(',')]

for sym in range(0,len(syms)):

    data = pd.read_csv(current_dir+'/'+base_file+'/'+ dir_raw +'/'+dir_raw +'_'+syms[sym]+'.csv')
    data[['stock_symbol','stock_code']] = data.Stock_Symbol.str.split("(",expand=True)

    data_out = pd.DataFrame({

        'company_name' : data['Company_Name'],
        'sector':  data['Sector'],
        'stock_symbol': data['stock_symbol'].str.replace(" ",""),
        'stock_code' : data['stock_code'].str.replace(")","")
    })

    data_out.to_csv(current_dir+'/'+base_file+'/'+dir_prefilter+'/'+dir_prefilter+'_'+syms[sym]+'.csv',index=False) 

