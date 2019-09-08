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
        hist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir1+"/"+in_dir1+'_'+comp_datalist['stock_symbol'][i]+'.csv')
        fcst = pd.read_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+"_"+comp_datalist['stock_symbol'][i]+'.csv')

        plt.scatter(hist['close'], fcst['yhat'], c='blue',marker='o')
        plt.xlabel('Actual Close Price')
        plt.ylabel('Predicted Close Price')
        plt.title(comp_datalist['stock_symbol'][i]+" Correlation Plot")
        plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_correlation_plot_'+comp_datalist['stock_symbol'][i]+'.png')
        #plt.show()
        plt.close()

    except:

        print(comp_datalist['stock_symbol'][i]+" is not found")