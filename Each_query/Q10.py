import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')

table_sort = df.sort_values('Profit', ascending = False)

df2 = table_sort['Order ID']

print(df2[0:1])