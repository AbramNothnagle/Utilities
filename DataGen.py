# -*- coding: utf-8 -*-
"""
Spyder Editor

Date: 11/22/24
Author: Abram Nothnagle
"""

'''
DataGen()
This class generates synthetic data for use in training neural networks
'''

import numpy as np
import pandas as pd
import math
#from operator import add
import operator

class DataGen():
    def __init__(self):
        self.custom_seed = False
    
    '''
    generateLinear(float slope, float intercept, float STDEV = 0, int start = 0, int stop, int step size)
    This function generates linear-like data. These data may be made stochastic by 
    giving it a standard deviation.
    Input:
        float slope: the slope m in y = mx + b
        float intercept: the y intercept b in y = mx + b
        float STDEV: the standard deviation to make the output random gaussian
        int start: the starting x value
        int stop: the ending x value
        int step_size: the step size to go from start to stop
    Output:
        (list of x, list of y)
    '''
    def generateLinear(self, m, b, stdev = 0, start = 0, stop = 100, step = 1):
        if (stop - start) < step:
            print("Error in generateLinear;\n step size is larger than data range.")
            return
        if stdev < 0:
            print("Error in generateLinear;\n stdev must be greater than 0.")
            return
        
        #initialize empty x and y lists that we can populate later
        x = []
        y = []
        for i in range(start, stop, step):
            y.append(m*i + b)
            x.append(i)
            
        #if a standard deviation was set, apply it to the y axis
        #This is the wrong way of applying this, it gives you a huge offset because it uses the overall average
        if stdev > 0:
            avg = np.mean(y) #first you need the average of the data
            noise = np.random.normal(avg, stdev, len(y))
            y = y + noise
            
        return (x, y)
    
    '''
    generateSine(float amplitude, float phase, float STDEV = 0, int start = 0, int stop, int step size)
    This function generates sine-like data. These data may be made stochastic by 
    giving it a standard deviation.
    Input:
        float amplitude: the amplitude A in y = A*sin(P*x) + offset
        float phase: the phase P in y = A*sin(P*x) + offset
        float offset: the offset in y = A*sin(P*x) + offset
        float STDEV: the standard deviation to make the output random gaussian
        int start: the starting x value
        int stop: the ending x value
        int step_size: the step size to go from start to stop
    Output:
        (list of x, list of y)
    '''
    def generateSine(self, a, p, offset, stdev = 0, start = 0, stop = 100, step = 1):
        if (stop - start) < step:
            print("Error in generateLinear;\n step size is larger than data range.")
            return
        if stdev < 0:
            print("Error in generateLinear;\n stdev must be greater than 0.")
            return
        
        #initialize empty x and y lists that we can populate later
        x = []
        y = []
        for i in range(start, stop, step):
            y.append(a*np.sin(p*i) + offset)
            x.append(i)
        
        #if a standard deviation was set, apply it to the y axis
        #This is the wrong way of applying this, it gives you a huge offset because it uses the overall average
        if stdev > 0:
            avg = np.mean(y) #first you need the average of the data
            noise = np.random.normal(avg, stdev, len(y))
            y = y + noise
            
        return (x, y)
    
    '''
    generateExponential(float[] data = None, float exponent, float STDEV = 0, float offset = 0, int start = 0, int stop, int step)
    This function generates exponential data by either incrementing from start to stop, or applying an exponent to an existing list.
    Input:
        float[] data: defaults to None. If not None, should be a float list that will have the exponent applied to it
        float exponent: exponent to be applied
        float STDEV: the standard deviation to make the output random gaussian
        float offset: offset to be applied to the output
        int start: the starting x value
        int stop: the ending x value
        int step: the step size to go from start to stop
    Output:
        (list of x, list of y)
    '''
    def generateExponential(self, data = None, exponent = 2, stdev = 0, offset = 0, start = 0, stop = 100, step = 1):
        if (stop - start) < step:
            print("Error in generateLinear;\n step size is larger than data range.")
            return
        if stdev < 0:
            print("Error in generateLinear;\n stdev must be greater than 0.")
            return
        
        #If data = None, then apply the exponential to a range from start to end with increment size
        if data == None:
            x = []
            y = []
            for i in range(start, stop, step):
                y.append(i**exponent + offset)
                x.append(i)
            #if a standard deviation was set, apply it to the y axis
            #This is the wrong way of applying this, it gives you a huge offset because it uses the overall average
            if stdev > 0:
                avg = np.mean(y) #first you need the average of the data
                noise = np.random.normal(avg, stdev, len(y))
                y = y + noise
        
        #If a data list was provided, apply the exponential to that list
        else:
            x = []
            y = []
            for i in range(len(data)):
                y.append(data[i]**exponent + offset)
                x.append(i)
            #if a standard deviation was set, apply it to the y axis
            #This is the wrong way of applying this, it gives you a huge offset because it uses the overall average
            if stdev > 0:
                avg = np.mean(y) #first you need the average of the data
                noise = np.random.normal(avg, stdev, len(y))
                y = y + noise
        
        return (x, y)
    
    '''
    combineFun(list a, list b, operator operation = add)
    This function combines two lists of the same dimensions through the corresponding operation.
    For example, to modify a linear plot with some sine-line deviation, you would
    call this function as combineFun(linear_data, sine_data, add) to add the sine
    wave to the linear graph.
    Hint: https://www.geeksforgeeks.org/python-map-function/
    Input:
        float list x: x values common to both a and b
        float list a: data of the first function to add. Must match dimensions of list b
        float list b: data of the second function to add. Must match dimensions of list a
        operator operation: the operation to combine the two. Add for noise, multiply for more complex, etc.
    Output:
        (list of x, list of y)
    '''
    def combineFun(self, x, a, b, operation = operator.add):
        y = list( map(operation, a, b) )
        return (x, y)
    
    '''
    applyWindowedNoise(list data, int window, float STD)
    This will apply noise to the data list using a normal distribution with standard deviation based on a rolling window.
    A rolling window will have the noise applied, so the noise follows the window instead of being calculated across all data.
    Uses backfill.
    Input: 
        list data: the data to have the STD applied over
        int window: rolling window that will have a normal distribution std applied to
        float STD: standard deviation used to generate the normal distribution in each window
    Output:
        list noisy_data: data of the same shape as data, but with the noise applied
    '''
    def applyWindowedNoise(self, data, window, std):
        df_data = pd.DataFrame(data)
        df_data['avgs'] = df_data[0].rolling(window = window, center = False).mean()
        df_data['avgs'] = df_data['avgs'].bfill()
        noisy_data = []
        for i in range(len(df_data)):
            #print(np.random.normal(df_data['avgs'].iloc[i], std))
            #noisy_data.append(df_data[0].iloc[i] + np.random.normal(df_data['avgs'].iloc[i], std))
            noisy_data.append(np.random.normal(df_data['avgs'].iloc[i], std))
        return noisy_data
    
    '''
    unitNorm(data)
    takes in the data and normalizes it to a unit norm for neural network training
    Input:
        list data: data to be normalized
    Output:
        list y_norm: normalized data. Same dimensions as input
    '''
    def unitNorm(self, data):
        min_val = np.min(data)
        max_val = np.max(data)
        return (data - min_val) / (max_val - min_val)
        ##normed = (data - data.min())/(data.max() - data.min()) #if usin Pandas
        #norm = np.linalg.norm(y, axis=0, keepdims=True)
        #return y / norm
