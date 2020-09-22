# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:14:41 2020

@author: phamk
"""


import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')

table_sort = df.sort_values('Customer Name')

#print(table_sort)
print(table_sort['Customer Name'])

table_sort.to_csv('modified.csv')