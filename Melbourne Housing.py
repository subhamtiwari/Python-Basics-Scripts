import pandas as pd


melbourne_file_path =(r"C:\Users\666677\Documents\Data-Sets\MELBOURNE_HOUSE_PRICES_LESS.csv")
data = pd.read_csv(melbourne_file_path)
data.columns

print(data)
data.describe()

data.columns

# dropna drops missing values (think of na as "not available")
data=data.dropna(axis=0)

#The data we need to predict as well 
y=data.Price



melbourne_features = [ 'Address', 'Rooms', 'Type', 'Method', 'SellerG',
       'Date', 'Postcode', 'Regionname', 'Propertycount', 'Distance',
       'CouncilArea']

x = data[melbourne_features]
x=pd.to_numeric(data[ 'Address', 'Rooms', 'Type', 'Method', 'SellerG',
       'Date', 'Postcode', 'Regionname', 'Propertycount', 'Distance',
       'CouncilArea'], downcast="float")

x.describe
x.head()

#Defining Sklearn for the model to run 

from sklearn.tree import DecisionTreeRegressor

#Define the model 
data_model=DecisionTreeRegressor(random_state=1)
data_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))





