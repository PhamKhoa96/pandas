import pandas as pd

df = pd.read_excel('Superstore.xls')

table_sort = df.sort_values('Order Date')

table_sort['Month'] = table_sort['Order Date'].dt.month
table_sort['Year'] = table_sort['Order Date'].dt.year

for x in range (1, 13):
    df3 = table_sort.loc[(table_sort['Month'] == x) & (table_sort['Year'] == 2018)]
    data = df3['Sales'].sum() 
    print('Our sales in month' , x ,'in 2018 is', data)