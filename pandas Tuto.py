# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:09:40 2020

@author: 666677
"""


import pandas as pd 
import numpy as np 
data=pd.DataFrame(data=np.arange(0,20).reshape(5,4), index=[1,3,3,3,5],columns=[1,2,3,4])

data.to_csv('test.csv')


#accesing the location of element 

# .loc - row index  .iloc - row and columns index

data.loc[3]

data.iloc[:3,:2]

#Converting the data frames in the arrays with .values 


data.iloc[:3,:2].values.shape

data.isnull().sum

data.count()

#dIFFERENT TYPES OF READING DATASETS 

