import pandas as pd

df = pd.read_excel('Superstore.xls')

data = df['Sales'].sum() 

print(data)