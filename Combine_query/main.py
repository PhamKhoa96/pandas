import pandas as pd
df = pd.read_excel('Superstore.xls')
#df = pd.read_csv('Superstore.csv')


#######################################Query1
print('\n##########################Query1####################################')
print('Sort customer names in alphabetical order.')
table_sort = df.sort_values('Customer Name')
#print(table_sort)
print(table_sort['Customer Name'])
table_sort.to_csv('modified.csv')


#######################################Query2
print('\n##########################Query2####################################')
print('How many customers do we have?')
dups_shape = df.pivot_table(index=['Customer Name'], aggfunc='size')
index = dups_shape.index
print(len(index))


#######################################Query3
print('\n##########################Query3####################################')
print('What were the revenue?')
data = df['Sales'].sum() 
print(data)


#######################################Query4
print('\n##########################Query4####################################')
print('What were our sales for the corporate segment?')
df2 = df[df['Segment'].str.contains("Corporate")]
data2 = df2['Sales'].sum()
print(data2)


#######################################Query5
print('\n##########################Query5####################################')
print('What were our sales by month in 2018?')
table_sort5 = df.sort_values('Order Date')
table_sort5['Month'] = table_sort5['Order Date'].dt.month
table_sort5['Year'] = table_sort5['Order Date'].dt.year
for x in range (1, 13):
    df3 = table_sort5.loc[(table_sort5['Month'] == x) & (table_sort5['Year'] == 2018)]
    data3 = df3['Sales'].sum() 
    print('Our sales in month' , x ,'in 2018 is', data3)
    
    
#######################################Query6
print('\n##########################Query6####################################')
print('What were sales in each state?')
import numpy as np
df6 = df.pivot_table(index=['State'], aggfunc={'Sales': np.sum})
print(df6)


#######################################Query7
print('\n##########################Query7####################################')
print('What were the top 5 cities based on sales?')
df7 = df.pivot_table(index=['City'], aggfunc={'Sales': np.sum})
table_sort7 = df7.sort_values('Sales', ascending = False)
print(table_sort7[0:5])


#######################################Query8
print('\n##########################Query8####################################')
print('How much profit did we make? By quarter?')
table_sort8 = df.sort_values('Order Date')
table_sort8['Year'] = table_sort8['Order Date'].dt.year
table_sort8['Month'] = table_sort8['Order Date'].dt.month
for y in range (0, 4):
    print('In' , (2015+y))
    for x in range (0, 4):
        df8 = table_sort8.loc[((table_sort8['Month'] > (0+3*x)) & (table_sort8['Month'] < (4+3*x)))
                         & (table_sort8['Year'] == (2015+y))]
        data = df8['Profit'].sum()         
        print ( 'Qtr' , x+1 , ' = ', data)
        

#######################################Query9
print('\n##########################Query9####################################')
print('What was the average profit per year?')
table_sort9 = df.sort_values('Order Date')
table_sort9['Year'] = table_sort9['Order Date'].dt.year
table_sort9['Month'] = table_sort9['Order Date'].dt.month
df9 = table_sort9.pivot_table(index=['Year'],
                    aggfunc={'Profit': np.mean,})
print(df9)


#######################################Query10
print('\n##########################Query10####################################')
print('Which orders had high profits?')
table_sort10 = df.sort_values('Profit', ascending = False)
df2 = table_sort10['Order ID']
print(df2[0:1])


#######################################Query11
print('\n##########################Query11####################################')
print('In California, what were the top 5 cities based on sales in 2018?')
df11 = df.sort_values('Order Date')
df11['Year'] = df11['Order Date'].dt.year
df12 = df11.loc[(df11['State'] == 'California') & (df11['Year'] == 2018)]
df13 = df12.pivot_table(index=['City'], aggfunc={'Sales': np.sum})
df14 = df13.sort_values('Sales', ascending = False)
print(df14[0:5])


#######################################Query12
print('\n##########################Query12####################################')
print('Compare revenue and profit ratio for each category and subcategory.')
df15 = df.pivot_table(index=['Category' , 'Sub-Category'], aggfunc={'Sales': np.sum, 'Profit': np.sum})
df15['Ratio'] = df15['Profit']/df15['Sales']
print(df15)