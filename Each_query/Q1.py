import pandas as pd

df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')

table_sort = df.sort_values('Customer Name')

#print(table_sort)
print(table_sort['Customer Name'])

table_sort.to_csv('modified.csv')