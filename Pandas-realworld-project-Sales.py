import pandas as pd
import os
data_sales=pd.read_csv('Sales_April_2019.csv')
test=pd.read_csv('Sales_April_2019.csv')

files=[file for file in os.listdir()]

for file in files:
    print(file)
    
all_months_data=pd.DataFrame()


for file in files:
    df=pd.read_csv(""+file)
    all_months_data=pd.concat([all_months_data,df])
    
all_months_data.to_csv("all_data.csv",index=False)

all_data=pd.read_csv("all_data.csv")
all_data.head()

#Adding a columns for the month 
#Finding the best sales for a month 

#Adding the month column with a value of 3 
all_data['Month']=3
all_data.head()

all_data['Month']=all_data['Order Date'].str[0:2]
all_data.head()
print(all_data['Month'])

all_months_data['Month'].head()
all_data['Month']=all_data['Month'].str.replace(',', '').astype(int)

all_data.dropna( inplace=True)

#Finding the nan values in the data set 


#invalid literal for int() with base 10: 'Or'
#Finding  the OR which is shooting the error message

or_df=all_data[all_data['Month'].str[0:2]=='OR']

New_df=all_data[all_data['Order Date'].str[0:2]!='OR']
all_data.head(10)


#Chaning the values to numeric from string for the numerica values 
all_data.dropna(inplace=True)

all_data.head()

#Getting the OR details which are preventing the 
or_df=all_data[all_data['Month']=='OR']
or_df[]

all_data=all_data['Month'].astype('int32')

all_data.head()
all_data.describe

all_data.dropna(inplace=True)
all_data['Month']=3

all_data.head
all_data['Month']=all_data['Month'].astype('int32')

#Checking the type of data tye the columns have in it 

all_data.info()

#Converting the values of the columns of the data type 
pd.to_numeric(all_data['Price Each'],downcast='float')

nan_df = all_data[all_data.isna().any(axis=1)]
display(nan_df.head())

all_data = all_data.dropna(how='all')
all_data.head()

#Get rid of text in order date column


all_data = all_data[all_data['Order Date'].str[0:2]!='Or']


#Make columns correct type


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


#all_data['Month 2'] = pd.to_datetime(all_data['Order Date']).dt.month
#all_data.head()

#Breaking down the address to get the city name from the 
all_data=




























