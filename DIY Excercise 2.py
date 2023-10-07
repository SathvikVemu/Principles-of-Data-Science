# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 19:02:08 2023

@author: sathv
"""
#Create an array of integers ranging from 5 to 15
import numpy as np
x = np.arange(5, 15)
print(x) # x returns the array


#The snippet below produces an array of seven evenly placed numbers between 0 and 23
n = np.linspace(0, 23, 7)
print(n)


#Array with uniform distribution
uni = np.random.uniform(-1, 1, size=None)
import matplotlib.pyplot as plt

plt.plot(uni)
plt.show() #to plot the uni distrubution array.

#Making two random arrays

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# finding sum of squares
sum_sq = np.sum(np.square(a - b))
 
# Doing squareroot and
# printing Euclidean distance
print(np.sqrt(sum_sq))

