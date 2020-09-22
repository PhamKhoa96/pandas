# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:08:51 2020

@author: phamk
"""


import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')

table_sort = df.sort_values('Order Date')
#df2 = df.filter(regex='spike')
print(table_sort)

df2 = table_sort[table_sort['Customer ID'].str.contains("DP")]

df2.to_csv('modified1.csv')