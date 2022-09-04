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
df['Week'].head(5)
#Cleaning data within each column with string values
df['District_Name'] = df['District_Name'].str.replace('[^A-Za-z0-9]+', '_')
df['Learning_Modality'] = df['Learning_Modality'].str.replace('[^A-Za-z0-9]+', '_')
df['City'] = df['City'].str.replace('[^A-Za-z0-9]+', '_')
df['State'] = df['State'].str.replace('[^A-Za-z0-9]+', '_')
#checking data has been cleaned by looking at first 15 rows of columns
df['District_Name'].head(15)
df['Learning_Modality'].head(15)
df['City'].head(15)
df['State'].head(15)

#counting white space and special characters in columns with string values
df['District_Name'].str.count(' ')
df['Learning_Modality'].str.count(' ')
df['City'].str.count(' ')
df['State'].str.count(' ')
df['District_Name'].str.count('[^A-Za-z0-9]+')
df['Learning_Modality'].str.count('[^A-Za-z0-9]+')
df['City'].str.count('[^A-Za-z0-9]+')
df['State'].str.count('[^A-Za-z0-9]+')

#looking at data type of each column
df.dtypes
# convert date column to datetime format
df['Week'] = pd.to_datetime(df['Week'])
df.dtypes #check again to make sure data type is correct
df['Week'].head(5) #preview of correct format

#checking for duplicate rows in data
df.duplicated()
df.drop_duplicates()

#counting missing values in the data
df.isnull().sum()

#creating a function that produces true statement if value in column meets criteria, if not then produce false statement
def A(Learning_Modality):
    if Learning_Modality == 'In_Person':
        return "true"
    else:
        return "false"
#applying the function in the new column
df['modality_inperson'] = df['Learning_Modality'].apply(A)
list(df) #checking the newly created column exists
df['modality_inperson'].tail(5) #checking the function works properly