# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:15:30 2020

@author: phamk
"""

import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')


df1 = df.sort_values('Order Date')
df1['Year'] = df1['Order Date'].dt.year
df2 = df1.loc[(df1['State'] == 'California') & (df1['Year'] == 2018)]
df3 = df2.pivot_table(index=['City'], aggfunc={'Sales': np.sum})
df4 = df3.sort_values('Sales', ascending = False)

print(df4[0:5])

