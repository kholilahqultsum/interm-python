import numpy as np

#Adding 1D elements
my_array = np.arange(11)
x = np.append(my_array, [11, 12, 13])
print(x)

#Append to 2D elements
my_array = np.array(([1,2,3], [4,5,6])) #(2,3)
x = np.append(my_array, [[7,8,9],[10,11,12], [13,14,15], [16,17,18]], axis = 0) #0 is row
print(x)

# my_array = np.array(([1,2,3], [4,5,6])) #(2,3)
x = np.append(my_array, [[7,8,9], [9,10,11]], axis = 1) #1 is coloumn
print(x) 

#concatenate: technique of combining two strings
my_array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
my_array2 = np.array([[10,11,12],[13,14,15],[16,17,18]])
x = np.concatenate((my_array1,my_array2), axis = 1)
print(x)
