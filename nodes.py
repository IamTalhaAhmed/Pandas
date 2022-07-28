'''
    length=len(df.Keyword)
    #print(length)
    for i in range(1,length+1):
        keyword=obj.data[i]['Keyword']
        

#Keyword,Country,Difficulty,Volume,CPC,CPS,Parent Keyword,Last Update,SERP Features,Global volume,Traffic potential
    
'''

import csv
import pandas as pd
df=pd.read_csv('data_sets/grpr_input.csv')
length=len(df.Keyword)

with open('data_sets/grpr_input.csv','r') as f:
    reader=csv.DictReader(f)
    data=list(reader)
#print(data[0]['Keyword'])


class Node:
    keyword=None
    country=None
    difficulty=None
    volume=None
    cpc=None
    cps=None
    pkey=None
    lUpdate=None
    serp=None
    gVol=None
    traffic=None
    
li=[]
for i in range(0,5):
    obj=Node()
    obj.keyword=data[i]['Keyword']
    obj.country=data[i]['Country']
    obj.difficulty=data[i]['Difficulty']
    obj.volume=data[i]['Volume']
    obj.cpc=data[i]['CPC']
    obj.cps=data[i]['CPS']
    obj.pkey=data[i]['Parent Keyword']
    obj.lUpdate=data[i]['Last Update']
    obj.serp=data[i]['SERP Features']
    obj.gVol=data[i]['Global volume']
    obj.traffic=data[i]['Traffic potential']
    li.append(obj)

print(li[3].keyword)