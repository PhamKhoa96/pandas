# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:38:03 2020

@author: phamk
"""

import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')

#print(df.dtypes)

table_sort = df.sort_values('Order Date')

table_sort['Year'] = table_sort['Order Date'].dt.year
table_sort['Month'] = table_sort['Order Date'].dt.month

#table_sort['Year'] == 2015

print(table_sort)

for y in range (0, 4):
    print('In' , (2015+y))
    for x in range (0, 4):
        df3 = table_sort.loc[((table_sort['Month'] > (0+3*x)) & (table_sort['Month'] < (4+3*x)))
                         & (table_sort['Year'] == (2015+y))]
        data = df3['Profit'].sum()         
        print ( 'Qtr' , x+1 , ' = ', data)