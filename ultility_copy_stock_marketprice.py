from distutils.dir_util import copy_tree
import os
import configparser 

parser = configparser.ConfigParser()
parser.read('config.ini')

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = parser.get('directory','base_dir')
portfolio_name = parser.get('portfolio_settings','portfolio_name')

selected = [e.strip() for e in parser.get('portfolio_settings','selection').split(',')]

in_dir = parser.get('directory','company_stock_marketprice_processed')
out_dir = parser.get('directory','portfolio_dir')

to_dir = current_dir+"/"+base_dir+"/"+out_dir+"/"+portfolio_name

for i in range(0,len(selected)):
    from_dir = current_dir+"/"+base_dir+"/"+ in_dir+"/"+selected[i]
    copy_tree(from_dir, to_dir)