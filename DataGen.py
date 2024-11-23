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
        float amplitude: the amplitude A in y = A*sin(P*x)
        float phase: the phase P in y = A*sin(P*x)
        float STDEV: the standard deviation to make the output random gaussian
        int start: the starting x value
        int stop: the ending x value
        int step_size: the step size to go from start to stop
    Output:
        (list of x, list of y)
    '''
    def generateSine(self, a, p, stdev = 0, start = 0, stop = 100, step = 1):
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
            y.append(a*np.sin(p*i))
            x.append(i)
        
        #if a standard deviation was set, apply it to the y axis
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
    '''
