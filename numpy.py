  import numpy as np 
a=np.array([0,1,2,3])
print(a)

print(np.arange(10))

l=range(1000)

%timeit [i**2 for i in l]



aa=3
%timeit print(aa**2)


#creating array 

a=np.array([1,2,3,4,5])

print(a)


#print dimension
a.ndim

a.shape

# 2- dimension array 

b=np.array([[1,2,3,4],[6,7,8,9,0]])

print(b)

#3 dimension arrays 
c=np.array([[1,2,3],[4,5,6],[6,7,8]])

c.shape

c.ndim


a=np.arange(10)
a


#START END NUMBER STEP : NO OF GAPS TO BE TAKEN

b=np.arange(1,10,3)
print(b)

#using linespace for the arranging the number s

a=np.linspace(0,1,6)
a

ones=np.ones((3,3))
ones




zeros=np.zeros((3,3))
zeros

eyes=np.eye(3)

s = np.array(['Ram', 'Robert', 'Rahim'])

s.dtype


a = np.diag([1, 2, 3])

print(a)

a[2,1]=5

#Slicing 

a=np.arange(10)

a
#Slicing syntax 
a[1:8:2]
a

#This will slice by step from 1 to 8 

#This is giving values to the 
a=np.arange(10)
a[5:]=10
print(a)

b = np.arange(5)
a[5:] = b[::-1]  #assigning

a





