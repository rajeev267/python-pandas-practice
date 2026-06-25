import pandas as pd
df = pd.DataFrame({'Category':['Mobile','Laptop','Mobile','Laptop'],'Sales':[10000,30000,15000,25000]})
print(df.groupby('Category')['Sales'].sum())
