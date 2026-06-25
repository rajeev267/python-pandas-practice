import pandas as pd
df = pd.DataFrame({'Department':['IT','HR','IT','Sales'],'Salary':[50000,40000,60000,45000]})
print(df.groupby('Department')['Salary'].mean())
