# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:45:02 2024

@author: abram
"""


import DataGen
import matplotlib.pyplot as plt
from operator import add

def testDataGen():
    generator = DataGen.DataGen()
    
    #TEST LINEAR GENERATION
    xl, yl = generator.generateLinear(1,0,1,10,90,2)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(xl, yl, label='Noisy Data')
    plt.legend()
    plt.title('Original Data vs. Noisy Data with Exponential Std Dev')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    #TEST SINE GENERATION
    xs, ys = generator.generateSine(2,0.30,0,10,90,2)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(xs, ys, label='Noisy Data')
    plt.legend()
    plt.title('Noisy sine data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    #TEST LINEAR MODIFIED BY SINE GENERATION
    #print(len(xl), len(xs))
    #print(len(yl), len(ys))
    #xb = list( map(add, xl, xs) )
    #yb = list( map(add, yl, ys) )
    x, y = generator.combineFun(xs, yl, ys, add)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label='Noisy Data')
    plt.legend()
    plt.title('Linear data with sine applied')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    return

def testNorm():
    generator = DataGen.DataGen()
    x, y = generator.generateLinear(1,0,1,10,90,2)
    #x, y = generator.generateSine(100,0.30,0,10,90,2)
    
    y_norm = generator.unitNorm(y)
    # Plotting original
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label='Original Data')
    plt.legend()
    plt.title('Original Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_norm, label='Normalized Data')
    plt.legend()
    plt.title('Normalized Data')
    plt.xlabel('x')
    plt.ylabel('normalized y')
    plt.show()

#testDataGen()
testNorm()