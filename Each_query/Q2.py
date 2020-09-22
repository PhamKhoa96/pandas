import pandas as pd

df = pd.read_excel('Superstore.xls')

dups_shape = df.pivot_table(index=['Customer Name'], aggfunc='size')

index = dups_shape.index

print(len(index))