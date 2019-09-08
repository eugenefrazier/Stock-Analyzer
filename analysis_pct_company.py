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

data = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+stock_symbol+'.csv')

x = data['date'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d'))
y = data['close'].pct_change()
plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Percentage Change %')
plt.title(stock_symbol+" Percentage Change Plot")
plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_pct_change_plot_'+stock_symbol+'.png')
plt.show(block=False)
plt.pause(6)
plt.close()
#plt.show()