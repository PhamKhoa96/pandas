# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:08:11 2020

@author: phamk
"""


import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')

df2 = df.pivot_table(index=['Category' , 'Sub-Category'], aggfunc={'Sales': np.sum, 'Profit': np.sum})
df2['Ratio'] = df2['Profit']/df2['Sales']

print(df2)
