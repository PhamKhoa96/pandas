# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:37:46 2020

@author: phamk
"""

import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')

#dups_shape = df.pivot_table(index=['State'], aggfunc='size')

dups_shape = df.pivot_table(index=['State'], aggfunc=np.sum)

print(dups_shape)

print(type(dups_shape))

index = dups_shape.index

#print(type(dups_shape.to_list()))

#print(dups_shape.columns)

tup = 'python', 'geeks'
print(type(tup))

#print(dups_shape)

#type(dups_shape)


#table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)


'''
for x in dups_shape:
    print(x)
'''

'''
for x in range (0, (len(index)-1)):
    print(dups_shape[1,:])
'''
