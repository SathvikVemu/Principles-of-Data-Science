# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:48:04 2023

@author: sathv
"""

import csv
import sys
import pandas as pd


file=pd.read_csv('TB_burden_countries_2014-09-29.csv') 
print(file)
print(len(file)) #This function can indicate the total number of rows in the csv file.


prevnum = []

with open("TB_burden_countries_2014-09-29.csv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        prevnum = row["e_prev_num_lo"]
        if num_lower is not None:
            prevnum.append(float(row["e_prev_num_lo"]))
            
avg_num = sum(prevnum)/ len(prevnum)

print("The average is:", avg_num) #This returns the average of the numerical values in the column "e_prev_num_lo"



