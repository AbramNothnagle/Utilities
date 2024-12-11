# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:40:53 2024

@author: anothnag
"""

import csv 
import numpy as np

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