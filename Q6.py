# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:37:46 2020

@author: phamk
"""

import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')

df2 = df.pivot_table(index=['State'], aggfunc={'Sales': np.sum})

print(df2)

