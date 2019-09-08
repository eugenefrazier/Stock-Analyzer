from datetime import datetime
import pandas as pd
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

dir_datalist = parser.get('directory','company_datalist_prefilter')
dir_raw = parser.get('directory','company_stock_marketprice_baseprice_raw')
dir_prefilter = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
base_file = parser.get('directory','base_dir')

in_datalist = current_dir+'/'+base_file+"/"+dir_datalist+"/"+dir_datalist
in_dir = current_dir+'/'+base_file+"/"+dir_raw
out_dir = current_dir+'/'+base_file+'/'+dir_prefilter

syms = [e.strip() for e in parser.get('general_settings','syms').split(',')]

current_date = datetime.now().strftime("%y-%m-%d")

for sym in range(0,len(syms)):

    comp_datalist = pd.read_csv(in_datalist+"_"+syms[sym]+".csv",dtype =str)

    for i in range(0,comp_datalist['stock_code'].count()):

        try:

            print("[Status]Prefiltering "+comp_datalist['stock_symbol'][i])
            data = pd.read_csv(in_dir+'/'+dir_raw+'_'+comp_datalist['stock_symbol'][i]+'.csv')
            filtered_data = data.dropna()
            filtered_data.to_csv(out_dir+"/"+dir_prefilter+'_'+comp_datalist['stock_symbol'][i]+'.csv',index=False) 
            
        
        except:
            
            print('[Status]stock_symbol is not found !')
