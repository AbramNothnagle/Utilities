# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:40:53 2024

@author: anothnag
"""

import csv 
import numpy as np
from StockCalculations import StockCalculator

spy = []
with open('spy_max.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        spy.append(row)
    print(len(spy))
    print(spy[0:10])

spyNumpy = np.array(spy)
print(spyNumpy[0:10])
print(np.sum(spyNumpy[1:5,1].astype(np.float)))

window = spyNumpy[1:5,1].astype(np.float)
weights = np.array(list(range(1,5)))
weights = weights/np.sum(weights)
print(window*weights)
print(np.std(spyNumpy[1:5,1].astype(np.float)))

print(np.max(spyNumpy[1:5,1].astype(np.float)))

#spyStockCalc = StockCalculator(spy, 'SPY')

import pandas as pd
spy_input = pd.read_csv('spy_max.csv')
#normalize
spy_input.drop('Date',axis=1,inplace=True)
spy_normed = (spy_input - spy_input.min())/(spy_input.max() - spy_input.min())
print(spy_normed.max())

#check the rows and columns all make sense
print(spy_input[10:20])
spy_input['SMA20'] = spy_input['Close/Last'].rolling(window = 20, center = False).mean()
print(spy_input[30:40])