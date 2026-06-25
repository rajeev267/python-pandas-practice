import pandas as pd
students = pd.DataFrame({'ID':[1,2],'Name':['Rajeev','Mayank']})
marks = pd.DataFrame({'ID':[1,2],'Marks':[85,90]})
print(pd.merge(students,marks,on='ID'))
