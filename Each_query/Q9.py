import numpy as np
import pandas as pd

df = pd.read_excel('Superstore.xls')

table_sort = df.sort_values('Order Date')

table_sort['Year'] = table_sort['Order Date'].dt.year
table_sort['Month'] = table_sort['Order Date'].dt.month

df3 = table_sort.pivot_table(index=['Year'],
                    aggfunc={'Profit': np.mean,})
print(df3)