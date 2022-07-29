import csv
import pandas as pd
import re
import sys

df=pd.read_csv('data_sets/'+sys.argv[1])            #41902
 
#the following line will check for the columns that have the null values and the number of null values in each column.
#print(df.isna().sum())    #13168

#removing rows with null values in keyword or volume
df=df.dropna(axis=0,how='any',subset=['Keyword','Volume'])

#replacing null values in CPC and CPS
df.CPC.fillna(value=1,inplace=True)
df.CPS.fillna(value=0.1,inplace=True)

#print(df[['CPC','CPS']])

#if coloumn values are having a range then to replace them with maximum value:
#column=pd.Series(df.column_name)

#cleaned=column.str.extract(pat= '(\d+$)')

#df=df.assign(column_name = cleaned)
#print(df)

df.to_csv('data_sets/output_grpr.csv',index=False) 