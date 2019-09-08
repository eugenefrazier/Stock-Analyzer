import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

stock_symbol = parser.get('general_settings','stock_symbol')
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

fcst = pd.read_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+"_"+stock_symbol+'.csv')
hist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+stock_symbol+".csv")

plt.plot(fcst['yhat'], label='Predicted Closed Price')
plt.plot(hist['close'],label='Actual Closed Price')
plt.xlabel('Date Index')
plt.ylabel('Close Price')
plt.title(stock_symbol+" Price Prediction")
plt.legend()
plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_predicted_'+stock_symbol+'.png')
#plt.show()
plt.show(block=False)
plt.pause(6)
plt.close()