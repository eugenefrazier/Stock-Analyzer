import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')
out_dir = parser.get('directory','portfolio_dir')

selected = [e.strip() for e in parser.get('portfolio_settings','selection').split(',')]
current_dir = os.path.dirname(os.path.realpath(__file__))

portfolio_name = parser.get('portfolio_settings','portfolio_name')

fig, ax1 = plt.subplots()

df0 = pd.read_csv(current_dir+"/"+base_dir+"/"+out_dir+'/'+portfolio_name+"/"+portfolio_name+"_total_closed_price.csv")
df1 = pd.read_csv(current_dir+'/dataset/KLSE_testbench.csv')

df0['date'] = df0['date'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d'))
df1['date'] = df1['date'].map(lambda x: datetime.strptime(str(x), '%m/%d/%y'))

ax1.plot(df0['date'], df0['close'], 'r-')
ax1.set_xlabel('date')

# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel(selected, color='r')
ax1.tick_params('y', colors='r')

ax2 = ax1.twinx()
ax2.plot(df1['date'], df1['close'], 'b-')
ax2.set_ylabel('KLCI', color='b')

ax2.tick_params('y', colors='b')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+portfolio_name+"/"+portfolio_name+'_performance_index.png')
plt.show(block=False)
plt.pause(5)
plt.close()