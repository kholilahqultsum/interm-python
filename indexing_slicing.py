import numpy as np

#Take specific number of array
my_array = np.array([1,2,3,4,5,6])
print(my_array[2:])

#Selecting values by conditions
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[x > 5])
print(x[x%2 == 0])
print(x[(x > 2) & (x < 11)])
print(x[(x > 5) | (x == 5)])