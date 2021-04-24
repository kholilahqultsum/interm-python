import numpy as np 

#1D data to 2D in rows
x = np.array([1,2,3,4,5])
x2 = x[np.newaxis, :]
print(x2)
print(x2.shape)

#1D data to 2D in coloumn
x = np.array([1,2,3,4,5])
x2 = x[:, np.newaxis]
print(x2) 
print(x2.shape)

#2D data to 3D data
x3 = x2[np.newaxis, :]
print(x3)
print(x3.shape) #(1,5,1)

x3 = x2[:, np.newaxis]
print(x3)
print(x3.shape) #(5,1,1)