import pandas as pd
df = pd.DataFrame({'Name':['A','B','C'],'Marks':[80,95,70]})
print(df.sort_values(by='Marks',ascending=False))
