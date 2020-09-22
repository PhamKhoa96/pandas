# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:29:26 2020

@author: phamk
"""


import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')

df2 = df.pivot_table(index=['City'], aggfunc={'Sales': np.sum})

table_sort = df2.sort_values('Sales', ascending = False)

print(table_sort[0:5])