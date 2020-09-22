# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:35:00 2020

@author: phamk
"""


import pandas as pd

#df = pd.read_csv('pokemon_data.csv')

df = pd.read_csv('pokemon_data.csv')

#print(df.head(3))
#print(df.tail(3))
#print(df)

## Read Headers
   #print(df.columns)
        
## Read each Column
   #print(df[['Name','Type 1','HP']][0:5])
   
## Read each Row
   #print(df.iloc[1:4])

## Read a specific location (R,C)
   #print(df.iloc[2,1])
   
## Iterate through each Row
# for index, row in df.iterrows():
#     print(index,row['Name'])

#print(df)

dups_shape = df.pivot_table(index=['Type 1'], aggfunc='size')

print(dups_shape)

index = dups_shape.index

print(len(index))