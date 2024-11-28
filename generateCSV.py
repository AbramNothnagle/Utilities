# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:58:33 2024

@author: abram
"""

import DataGen
import csv
import numpy as np

def generateNNData1():
    generator = DataGen.DataGen()
    
    #Create a sine-modified linear dataset for use in practice neural networks
    #13,000 datapoints to start
    #10,000 for training, 3,000 for testing
    x, y = generator.generateLinear(1, 0, 1, 1, 13000)
    sinex, siney = generator.generateSine(10, 0.3, 0, 1, 13000)
    x, y = generator.combineFun(x, y, siney) #adding
    y = generator.unitNorm(y) #normalize for training
    
    #Save data to .csv
    np.savetxt('outputs//generateNNData1.csv', np.vstack((x,y)).T, delimiter=', ')
    
    return

def writeToCSV(x, y, filename):
    new_list = zip(x, y)
    with open('file1.csv', 'wb+') as csvfile:
         filewriter = csv.writer(csvfile)
         filewriter.writerows(new_list)
    
generateNNData1()