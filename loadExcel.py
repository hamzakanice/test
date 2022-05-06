import pandas as pd
data=  pd.read_excel (r'MyData.xlsx')
#print(data)
df=pd.DataFrame(data)
#print (df)

for row in df.iterrows():
    print (row[1][0],row[1][1],row[1][2])
