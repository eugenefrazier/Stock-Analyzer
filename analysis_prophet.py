import pandas as pd
from fbprophet import Prophet
import numpy as np
from datetime import datetime
import os
import matplotlib.pyplot as plt
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))

#interesting date - 2014/15-01-01
stock_symbol = parser.get('general_settings','stock_symbol')
base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')
prophet_query = parser.get('query','prophet_query')

data = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+stock_symbol+".csv",dtype =str)
date_query  =  data['date'] <= prophet_query 

df = pd.DataFrame({
    'y': np.array(data['close'][date_query], dtype='float'),
    'ds': np.array(data['date'][date_query].map(lambda x: datetime.strptime(str(x),'%Y-%m-%d' )))
    })

length = data['close'].count()-data['close'][date_query].count()

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=length)
forecast = m.predict(future)

forecast.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+"_"+stock_symbol+'.csv',index=False)
m.plot(forecast)
m.plot(forecast).savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_prediction_'+stock_symbol+'.png')