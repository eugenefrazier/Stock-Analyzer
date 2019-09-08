import os
import pandas as pd
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_datalist_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

syms = [e.strip() for e in parser.get('general_settings','syms').split(',')]

for sym in range(0,len(syms)):

    comp_datalist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+syms[sym]+".csv",dtype =str)

    for i in range(0,comp_datalist['stock_code'].count()):

        os.mkdir(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]) 