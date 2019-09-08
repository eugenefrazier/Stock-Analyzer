import pandas as pd 
import matplotlib.pyplot as plt
import numpy
import os
import configparser

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')

in_dir = parser.get('directory','company_stock_marketprice_baseprice_raw')
out_dir = parser.get('directory','portfolio_dir')

portfolio_name = parser.get('portfolio_settings','portfolio_name')

selected = [e.strip() for e in parser.get('portfolio_settings','selection').split(',')]
data0 = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+selected[0]+'.csv')
data1 = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+selected[1]+'.csv')
data2 = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+selected[2]+'.csv')
data3 = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+"_"+selected[3]+'.csv')

df= pd.DataFrame({
    selected[0] : data0['close'],
    selected[1] : data1['close'],
    selected[2] : data2['close'],
    selected[3] : data3['close'],
})


correlations = df.corr()

print("\n")
print("Computing Pearson Correlation")
print(df.corr(method ='pearson'))

print("\n")
print("Computing Kendall Correlation")
print(df.corr(method ='kendall'))

print("\n")
print("Computing Spearman Correlation")
print(df.corr(method ='spearman'))
print("\n")


fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,len(selected),1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(selected)
ax.set_yticklabels(selected)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+portfolio_name+"/"+portfolio_name+'_correl_graph.png')
plt.show(block=False)
plt.pause(5)
plt.close()
