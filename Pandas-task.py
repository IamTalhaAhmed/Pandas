
# from the dataset i had to get the unique cutomer ids and then i was to make a new dataframe that would have a name for every customer id."
   
#importing pandas,
import csv
import pandas as pd
import string
import random 

#loading the dataframe
data=pd.read_csv("data_sets/data.csv",encoding= 'unicode_escape')

#getting the required coloumn of (unique)IDs from the dataframe in the list datastucture\n",
C_ID=list(data['CustomerID'].unique())

#getting the length of the list so that the asme number of rows of random data can be generated 
length=len(C_ID)

#function to generate random string data to fill up the names coloumn
def nameGenerator(size=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

#creating an empty list
names=[]

#calling the function to create the sample names 
for i in range(0,length):
    x=nameGenerator()
    names += [x]                            #adding the generated names to a list   

#to create a dataframe from the lists making a dictionary first\n",
dictionary={'CustomerID':C_ID,'Name':names}

sampledf=pd.DataFrame(dictionary)

sampledf.to_csv('data_sets/createdDF.csv',index=False)
'''
header=['CustomerID','Name']
#to write the created dataframe to a csv file
#step1:open the file in write mode 
with open("data_sets/createdDF.csv", 'w',encoding='UTF8',newline='') as f:

#step2:create a csv writer
    writer=csv.DictWriter(f,fieldnames=header)

#step3:write the file
    writer.writeheader()
 
    writer.writerows(dictionary)

    '''
