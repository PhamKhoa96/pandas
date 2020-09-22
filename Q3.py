# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:14:49 2020

@author: phamk
"""


import pandas as pd

df = pd.read_excel('Superstore.xls')

data = df['Sales'].sum() 

print(data)