# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:36:12 2020

@author: phamk
"""


import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')

#print(df.dtypes)

table_sort = df.sort_values('Order Date')

table_sort['Year'] = table_sort['Order Date'].dt.year
table_sort['Month'] = table_sort['Order Date'].dt.month

df3 = table_sort.pivot_table(index=['Year'],
                    aggfunc={'Profit': np.mean,})
print(df3)