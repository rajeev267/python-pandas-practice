import pandas as pd
df = pd.DataFrame({'Name':['A','A','B'],'Marks':[80,80,70]})
print(df.drop_duplicates())
