import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')
portfolio_name = parser.get('portfolio_settings','portfolio_name')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')

in_dir = parser.get('directory','portfolio_dir')

df = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+'/'+portfolio_name+"/"+portfolio_name+"_generated.csv")
fig, (ax1, ax2) = plt.subplots(1, 2)

# find min Volatility & max sharpe values in the dataframe (df)
min_volatility = df['Volatility'].min()
max_sharpe = df['Sharpe Ratio'].max()

# use the min, max values to locate and create the two special portfolios
sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
min_variance_port = df.loc[df['Volatility'] == min_volatility]

#print("\nSharpe Ratio Based Portfolio\n"+str(sharpe_portfolio.T))
#print("\nLow Variance Based Portfolio\n"+str(min_variance_port.T))

min_var_weight = [x for x in (min_variance_port.values[0][3:])]
min_var_data = [float(x) for x in min_var_weight]

sharpe_weight = [x for x in (sharpe_portfolio.values[0][3:])]
sharpe_data = [float(x) for x in sharpe_weight]

min_var_assets = [x.replace("Weight","") for x in (min_variance_port.columns.values[3:])]
sharpe_assets = [x.replace("Weight","") for x in (sharpe_portfolio.columns.values[3:])]

def func(pct, allvals):
    return "{:.1f}%\n".format(pct)

wedges1, texts1, autotexts1 = ax1.pie(min_var_data, autopct=lambda pct: func(pct,min_var_data),textprops=dict(color="w"))
wedges2, texts2, autotexts2 = ax2.pie(sharpe_data, autopct=lambda pct: func(pct,sharpe_data),textprops=dict(color="w"))

ax1.legend(wedges1, min_var_assets,title="Asset Allocation",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
ax2.legend(wedges2, sharpe_assets,title="Asset Allocation",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))

ax1.set_title("Low Risk Asset Allocation")
ax2.set_title("High Risk Asset Allocation")

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.savefig(current_dir+"/"+base_dir+"/"+in_dir+'/'+portfolio_name+"/"+portfolio_name+'_stock_allocation.png')
plt.show(block=False)
plt.pause(5)
plt.close()