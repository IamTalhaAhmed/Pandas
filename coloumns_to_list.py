import pandas as pd
import csv

#will store multiple links for 1 keyword as a list
data = pd.read_csv('data_sets/group_input_new.csv')
#print(data)
length=len(data.Keyword)
#print(length)
links=[]
check=0
i=0
while(i<length):   
    key=data.iat[i,0]
    li=[]
    for j in range(i,length):
        key_next=data.iat[j,0]
        
        if (key==key_next):
            link=data.iat[j,2]
            li.append(link)
        else:
            i=j
            links.append(li)
            break
        if (j==length-1):
            links.append(li)
            i=j+1
#print(links)
#print(len(links))
list_of_links=pd.Series(links)
#print(type(list_of_links))
data. drop(['Link','Position','Title','Snippet','Primary Intents','Secondary Intents','Client Ranking URL','Client Ranking Position','Client URL Ranking Count','CPC','CPS','Difficulty','Current Traffic','Potential Traffic','Current Value','Potential Value','Fibonacci Helper','Value Opportunity','Volume Opportunity','Competitor Score','Competitor ranking count','Related Results Count'], axis=1, inplace=True)
data.drop_duplicates(inplace=True)
data.reset_index(drop=True,inplace=True)
#print(data)

data['links']=list_of_links
print(data)

#writing the requires result to a csv file
#data.to_csv('data_sets/group_output_news.csv')

#>Task:storing the output data as a node structure
df=pd.read_csv('data_sets/group_output_news.csv')
length=len(df.Keyword)

with open('data_sets/group_output_news.csv','r') as f:
    reader=csv.DictReader(f)
    data_frame=list(reader)

#print(data_frame)
#Names of Coloumns:Keyword,Volume,links
class Node:
    keyword=None
    volume=None
    link=None

    
node_list=[]
for i in range(0,length):
    obj=Node()
    obj.keyword=data_frame[i]['Keyword']
    obj.volume=data_frame[i]['Volume']
    obj.link=data_frame[i]['links']
    node_list.append(obj)

#print(node_list[0].link)