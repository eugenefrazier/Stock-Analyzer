"""
Anomaly Detection (ad) Using hp filter and mad test

liubenyuan <liubenyuan@gmail.com>
"""

import numpy as np
import pandas as pd
from scipy import sparse, stats
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

df= pd.read_csv(current_dir+"/"+base_dir+"/"+in_dir+"/"+in_dir+'_'+stock_symbol+'.csv')

data = pd.DataFrame({'date': df['date'].map(lambda x: datetime.strptime(str(x),'%Y-%m-%d'))})

# Hodrick Prescott filter
def hp_filter(x, lamb=5000):
    w = len(x)
    b = [[1]*w, [-2]*w, [1]*w]
    D = sparse.spdiags(b, [0, 1, 2], w-2, w)
    I = sparse.eye(w)
    B = (I + lamb*(D.transpose()*D))
    return sparse.linalg.dsolve.spsolve(B, x)


def mad(data, axis=None):
    return np.mean(np.abs(data - np.mean(data, axis)), axis)


def AnomalyDetection(x, alpha=0.2, lamb=5000):
    """
    x         : pd.Series
    alpha     : The level of statistical significance with which to
                accept or reject anomalies. (expon distribution)
    lamb      : penalize parameter for hp filter
    return r  : Data frame containing the index of anomaly
    """
    # calculate residual
    xhat = hp_filter(x, lamb=lamb)
    resid = x - xhat

    # drop NA values
    ds = pd.Series(resid)
    ds = ds.dropna()

    # Remove the seasonal and trend component,
    # and the median of the data to create the univariate remainder
    md = np.median(x)
    data = ds - md

    # process data, using median filter
    ares = (data - data.median()).abs()
    data_sigma = data.mad() + 1e-12
    ares = ares/data_sigma

    # compute significance
    p = 1. - alpha
    R = stats.expon.interval(p, loc=ares.mean(), scale=ares.std())
    threshold = R[1]

    # extract index, np.argwhere(ares > md).ravel()
    r_id = ares.index[ares > threshold]

    return r_id


# demo
def main():

    # fix
    np.random.seed(42)

    # sample signals
    N = 1024  # number of sample points
    t = data['date']
    y = df['close']

    # outliers are assumed to be step/jump events at sampling points
    M = 3  # number of outliers
    for ii, vv in zip(np.random.rand(M)*N, np.random.randn(M)):
        y[int(ii):] += vv

    # detect anomaly
    r_idx = AnomalyDetection(y, alpha=0.1)

    #for x in range(0,len(r_idx)):
      #  print('Abnormality Detect on '+str(data['date'][r_idx[x]]))

    # plot the result
    plt.xlabel('Date')
    #plt.plot(y, 'b-')
    plt.plot(data['date'][r_idx], y[r_idx], 'ro')
 
    plt.twinx()
    plt.ylabel("Price")
    plt.tick_params(axis="y")
    plt.ylabel("Price")
    plt.plot(data['date'], df['close'], "b-", linewidth=1)
    plt.title(stock_symbol+" Anomaly Graph")
    #plt.show()
    plt.savefig(current_dir+"/"+base_dir+"/"+out_dir+'/'+stock_symbol+"/"+out_dir+'_anomaly_'+stock_symbol+'.png')
    plt.show(block=False)
    plt.pause(6)
    plt.close()

if __name__ == "__main__":
    main()