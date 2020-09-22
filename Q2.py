# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:14:46 2020

@author: phamk
"""


import pandas as pd

df = pd.read_excel('Superstore.xls')

dups_shape = df.pivot_table(index=['Customer Name'], aggfunc='size')

index = dups_shape.index

print(len(index))