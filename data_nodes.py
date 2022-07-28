import csv
import pandas as pd
df=pd.read_csv('data_sets/grpr_input.csv')
length=len(df.Keyword)

with open('data_sets/grpr_input.csv','r') as f:
    reader=csv.DictReader(f)
    data=list(reader)
#print(data[0]['Keyword'])
#Names of Coloumns:Keyword,Country,Difficulty,Volume,CPC,CPS,Parent Keyword,Last Update,SERP Features,Global volume,Traffic potential

class Node:
    keyword=None
    country=None
    difficulty=None
    volume=None
    cpc=None
    cps=None
    parent_keyword=None
    last_update=None
    serp_features=None
    global_volume=None
    traffic_potential=None
    
li=[]
for i in range(0,length):
    obj=Node()
    obj.keyword=data[i]['Keyword']
    obj.country=data[i]['Country']
    obj.difficulty=data[i]['Difficulty']
    obj.volume=data[i]['Volume']
    obj.cpc=data[i]['CPC']
    obj.cps=data[i]['CPS']
    obj.parent_keyword=data[i]['Parent Keyword']
    obj.last_update=data[i]['Last Update']
    obj.serp_features=data[i]['SERP Features']
    obj.global_volume=data[i]['Global volume']
    obj.traffic_potential=data[i]['Traffic potential']
    li.append(obj)

#print(li[3].keyword)