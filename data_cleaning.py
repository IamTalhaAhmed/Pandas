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