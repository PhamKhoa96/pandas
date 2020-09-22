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
    for x in range (0, 4):
        df3 = table_sort.loc[((table_sort['Month'] > (0+3*x)) & (table_sort['Month'] < (4+3*x)))
                         & (table_sort['Year'] == (2015+y))]
        data = df3['Profit'].sum() 

        print(data)
    print(2015+y)



'''
for x in range (0, 3):
    df3 = table_sort.loc[(table_sort['Month'] > x) 
                         & (table_sort['Month'] < (x+4))
                         & (table_sort['Year'] == 2015)]
    print (df3)
df3.to_csv('modified100.csv')
'''


    #df4 = df3.pivot_table(index=['Month'], aggfunc={'Profit': np.sum})
    #print(df4)


'''
for x in range (1, 9994):
    print(table_sort[1,'Month'])
'''

'''
if table_sort['Month'] = 1:
    table_sort['Qtr'] = Qtr1
'''
    
    
    
'''
df4 = table_sort.pivot_table(index=['Year','Month'], aggfunc={'Profit': np.sum})

print(df4)
print(type(df4))

print(df4.head())
'''



'''
df5 = df4.loc[(df4['Month'] > 0) 
                     & (df4['Month'] <4) 
                     & (df4['Year'] == 2015)]
print(df5)

df5.to_csv('modified11.csv')
'''



'''
for x in range (1, 12):
    df3 = table_sort.loc[(table_sort['Month'] == x) & (table_sort['Year'] == 2015)]
    df4 = df3.pivot_table(index=['Month'], aggfunc={'Profit': np.sum})
    print(df4)
'''



    
#m = np.asarray(data, dtype=np.float64)
#h = m.tolist()

#print(len(m))
'''
print(type(m))

thislist = ["apple", "banana", "cherry"]
print(type(thislist))
print(thislist[0])
'''