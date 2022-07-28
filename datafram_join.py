import pandas as pd
data1=pd.read_csv("data_sets/createdDF.csv")
data2=pd.read_csv("data_sets/data.csv",encoding='unicode_escape')

data=data2.merge(data1,how='left',on='CustomerID').reset_index(drop=True)
print(data)