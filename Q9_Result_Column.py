import pandas as pd
df = pd.DataFrame({'Name':['A','B','C'],'Marks':[80,35,70]})
df['Result']=df['Marks'].apply(lambda x:'Pass' if x>=40 else 'Fail')
print(df)
