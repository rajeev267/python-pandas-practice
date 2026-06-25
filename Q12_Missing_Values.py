import pandas as pd
df = pd.DataFrame({'Marks':[80,None,70]})
print(df.isnull().sum())
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df)
