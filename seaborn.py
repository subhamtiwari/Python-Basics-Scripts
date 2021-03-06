import seaborn as sns
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

a=sns.load_dataset("flights")
sns.relplot(x="passengers" , y="month",data=a)

#adding the3rd variable 
sns.relplot(x="passengers",y="month",hue="year", data=a)

#line plot with a different data set 

b=sns.load_dataset("tips")
sns.relplot(x="time",y="tip",data=b,kind="line")

#3rd type of use of seaborn for plotting catogerical variable 
#catplot 
sns.catplot(x="time",y="tip",data=b)

#differet kind of catplot :violin
sns.catplot(x="time",y="tip",data=b,kind="violin")

#diferent kind of catplot : boxen

sns.catplot(x="time", y="tip",data=b,kind="boxen") 

c=np.random.normal(loc=5,size=100,scale=2)
sns.distplot(c)


#Mutliple grid-graphs 
a=sns.load_dataset("iris")
b=sns.FacetGrid(a,col="species")
b.map(plt.hist,"sepal_length")

#Paired for multiple variables 


a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)

sns.set(style="darkgrid")
a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)



