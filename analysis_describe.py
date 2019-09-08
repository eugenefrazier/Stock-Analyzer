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

print("\n")
print("Calculating Closing Price of "+stock_symbol)
print(data['close'].describe())

print("\n")
print("Calculating Volume of "+stock_symbol)
print(data['volume'].describe())