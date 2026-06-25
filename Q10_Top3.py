import pandas as pd
df = pd.DataFrame({'Name':['A','B','C','D'],'Marks':[80,95,70,88]})
print(df.nlargest(3,'Marks'))
