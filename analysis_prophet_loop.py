import pandas as pd
from fbprophet import Prophet
import numpy as np
from datetime import datetime
import os
import matplotlib.pyplot as plt
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

#interesting date - 2014/15-01-01

current_dir = os.path.dirname(os.path.realpath(__file__))

base_dir = parser.get('directory','base_dir')
in_dir = parser.get('directory','company_datalist_prefilter')
in_dir1 = parser.get('directory','company_stock_marketprice_baseprice_prefilter')
out_dir = parser.get('directory','company_stock_marketprice_processed')
prophet_query = parser.get('query','prophet_query')

comp_datalist = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_combined.csv")

for i in range(0,comp_datalist['stock_symbol'].count()):
    try:

        print("Processing "+comp_datalist['stock_symbol'][i])
        data = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir1+"/"+in_dir1+'_'+comp_datalist['stock_symbol'][i]+'.csv')
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

        forecast.to_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+"_"+comp_datalist['stock_symbol'][i]+'.csv',index=False)
        #m.plot(forecast)
        #m.plot(forecast).savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+comp_datalist['stock_symbol'][i]+"/"+out_dir+'_prediction_'+comp_datalist['stock_symbol'][i]+'.png')

    except:

        print(comp_datalist['stock_symbol'][i]+" is not found")