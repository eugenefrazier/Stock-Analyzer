import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_datalist_prefilter')
in_dir1 = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

comp_datalist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_combined.csv")

for i in range(0,comp_datalist['stock_symbol'].count()):
   

    try:

        data = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir1+"/"+in_dir1+'_'+comp_datalist['stock_symbol'][i]+'.csv')
        print("[Status]Plotting Percentage Change of "+ comp_datalist['stock_symbol'][i])
        x = data['date'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d'))
        y = data['close'].pct_change()
        plt.plot(x,y)
        plt.xlabel('Date')
        plt.ylabel('Percentage Change %')
        plt.title(comp_datalist['stock_symbol'][i]+" Percentage Change Plot")
        plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_pct_change_plot_'+comp_datalist['stock_symbol'][i]+'.png')

    
    except:
        print("[Status]Error "+comp_datalist['stock_symbol'][i]+" is not found")
