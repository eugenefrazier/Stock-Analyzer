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


for i in range(0,comp_datalist['stock_code'].count()):

    try:

        print("[Status]Generating price prediction graph for "+comp_datalist['stock_symbol'][i])  
        hist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir1+"/"+in_dir1+'_'+comp_datalist['stock_symbol'][i]+'.csv')
        fcst = pd.read_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+"_"+comp_datalist['stock_symbol'][i]+'.csv')

        plt.plot(fcst['yhat'], label='Predicted Closed Price')
        plt.plot(hist['close'],label='Actual Closed Price')
        plt.xlabel('Date Index')
        plt.ylabel('Close Price')
        plt.title(comp_datalist['stock_symbol'][i]+" Price Prediction")
        plt.legend()
        plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_prediction_plot_'+comp_datalist['stock_symbol'][i]+'.png')
        #plt.show()
        plt.close()
    
    except:
        print("[Status]Error ! Unable to generate price prediction for "+comp_datalist['stock_symbol'][i])