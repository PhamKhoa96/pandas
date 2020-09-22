# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:08:51 2020

@author: phamk
"""


import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')

df2 = df[df['Segment'].str.contains("Corporate")]

data = df2['Sales'].sum()

print(data)