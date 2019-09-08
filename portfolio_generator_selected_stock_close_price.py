import pandas as pd
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')


in_dir = parser.get('directory','portfolio_dir')

selected = [e.strip() for e in parser.get('portfolio_settings','selection').split(',')]
portfolio_name = parser.get('portfolio_settings','portfolio_name')

data = pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+'/'+portfolio_name+"/"+portfolio_name+"_selection.csv")

clean = data.set_index('date')
table = clean.pivot(columns='ticker',values='close')
table['new'] =table[selected[0]]+table[selected[1]]+table[selected[2]]+table[selected[3]]


df = pd.DataFrame({
    'close':table['new']
 })
df.to_csv(current_dir+"/"+base_dir+"/"+in_dir+'/'+portfolio_name+"/"+portfolio_name+"_total_closed_price.csv")

