from datetime import datetime
import pandas as pd
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

dir_raw = parser.get('directory','company_fund_marketprice_raw')
dir_prefilter = parser.get('directory','company_fund_marketprice_prefilter')
base_file = parser.get('directory','base_dir')

in_dir = current_dir+'/'+base_file+'/'+dir_raw+'/'+dir_raw+'_'
out_dir = current_dir+'/'+base_file+'/'+dir_prefilter+'/'+dir_prefilter+'_'

syms = [e.strip() for e in parser.get('general_settings','syms').split(',')]

current_date = datetime.now().strftime("%y-%m-%d")

for sym in range(0,len(syms)):

    data = pd.read_csv(in_dir+str(current_date)+'/company_fund_marketprice_raw_'+str(current_date)+'_'+syms[sym]+'.csv',dtype=str)

    print("\n[Status]Running Prefiltering Script Symbol "+syms[sym]+"\n")
    filtered_data = data.dropna()

    df =pd.DataFrame({

        'stock_symbol': filtered_data['Stock_Symbol'].str.strip("Share Price Movement"),
        'mcap': filtered_data['market_capital'].str.strip(":"),
        'num_of_share':filtered_data['num_share'].str.strip(":"),
        'eps':filtered_data['eps'].str.strip(":"),
        'pe_ratio':filtered_data['pe_ratio'].str.strip(":"),
        'roe':filtered_data['roe'].str.strip(":"),
        'div':filtered_data['div'].str.strip(": ^"),
        'div_y':filtered_data['div_y'].str.strip(":"),
        'div_p':filtered_data['div_p'].str.strip(":"),
        'nta':filtered_data['nta'].str.strip(":"),
        'par_v':filtered_data['par_v'].str.strip(":")
        
    })
    
    print("\n[Status]Prefiltering Done !\n")
    print("\n[Status]Save to "+ out_dir+str(current_date)+'/'+dir_prefilter+'_'+str(current_date)+'_'+syms[sym]+'.csv\n')
    df.to_csv(out_dir+str(current_date)+'/'+dir_prefilter+'_'+str(current_date)+'_'+syms[sym]+'.csv',index=False) 

    