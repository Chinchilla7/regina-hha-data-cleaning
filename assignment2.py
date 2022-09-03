#install necessary package for assignment
import pandas as pd
import datetime

#load in csv data from healthdata.gov
df = pd.read_csv('data/School_Learning_Modalities.csv')

#getting the number of rows and columns in data
df.shape
print (df.shape)

#getting the column names in the data
list(df)
print(list(df))

# cleaning column names by eliminating special characters and white space
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
list(df) #to check renamed columns

#Cleaning data within each column with string values
df['District_Name'] = df['District_Name'].str.replace('[^A-Za-z0-9]+', '_')
df['Learning_Modality'] = df['Learning_Modality'].str.replace('[^A-Za-z0-9]+', '_')
df['City'] = df['City'].str.replace('[^A-Za-z0-9]+', '_')

df['City'].head(15)
