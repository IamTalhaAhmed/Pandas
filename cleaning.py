import csv
import pandas as pd

df=pd.read_csv('data_sets/grpr_input.csv')            #41902
 
#the following line will check for the columns that have the null values and the number of null values in each column.
#print(df.isna().sum())    #13168

#removing rows with null values in keyword or volume
df=df.dropna(axis=0,how='any',subset=['Keyword','Volume'])

#replacing null values in CPC and CPS
df.CPC.fillna(value=1,inplace=True)
df.CPS.fillna(value=0.1,inplace=True)
#print(df[['CPC','CPS']])

df.to_csv('data_sets/output_grpr.csv',index=False)

#Keyword,Country,Difficulty,Volume,CPC,CPS,Parent Keyword,Last Update,SERP Features,Global volume,Traffic potential
'''
class Node:
    def __init__(self,data,row):
        self.data=data
        self.row=row

    def getKeyword():    
        keyword=obj.data[obj.row]['Keyword']
        return keyword

    def getCountry():
        country=obj.data[obj.row]['Country']
        return keyword

    def getDifficulty():
        difficulty=obj.data[obj.row]['Difficulty']
        return difficulty

    def getVolume():    
        volume=obj.data[obj.row]['Volume']
        return volume

    def getCPC():    
        cpc=obj.data[obj.row]['CPC']
        return cpc

    def getCPS():
        cps=obj.data[obj.row]['CPS']
        return cps

    def getParentKey():
        pkey=obj.data[obj.row]['Parent Keyword']
        return pkey

    def getLastUpdate():
        lUpdate=obj.data[obj.row]['Last Update']
        return lUpdate

    def getSerpFeatures():
        serp=obj.data[obj.row]['SERP Features']
        return serp

    def getGlobalVol():
        gVol=obj.data[obj.row]['Global volume']
        return gVol

    def getTrafficPotenital():
        traffic=obj.data[obj.row]['Traffic potential']
        return traffic
    

with open('data_sets/grpr_input.csv','r') as f:
    reader=csv.DictReader(f)
    data=list(reader)
    obj=Node(data)
    keyword=Node.getKeyword()
    

'''
