import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import configparser
from sklearn import metrics

parser = configparser.ConfigParser()
parser.read('config.ini')

stock_symbol = parser.get('general_settings','stock_symbol')
current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')

fcst = pd.read_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+"_"+stock_symbol+'.csv')
hist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+stock_symbol+".csv")

new_data = pd.DataFrame({
    'fcst_new':fcst["yhat"],
    'hist_new':hist['close']
})

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) 

rmse = np.sqrt(metrics.mean_squared_error(new_data['hist_new'],new_data['fcst_new']))

mape = mean_absolute_percentage_error(new_data['hist_new'],new_data['fcst_new'])

print("\n")
print("[Status]Generating Statistical Analysis")
print("\n")
print("The value of Mean Absolute Percentage Error for "+stock_symbol+" is "+str(mape))
print("\n")
print("The value of Root Mean Squared Error for "+stock_symbol+" is "+str(rmse))
print("\n")
print("Computing Pearson Correlation")
print(new_data.corr(method ='pearson'))

print("\n")
print("Computing Kendall Correlation")
print(new_data.corr(method ='kendall'))

print("\n")
print("Computing Spearman Correlation")
print(new_data.corr(method ='spearman'))
print("\n")

plt.scatter(hist['close'], fcst['yhat'])
plt.xlabel('Actual Close Price')
plt.ylabel('Predicted Close Price')
plt.title(stock_symbol+" Correlation Plot")
plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_correlation_plot_'+stock_symbol+'.png')
plt.show(block=False)
plt.pause(6)
plt.close()
