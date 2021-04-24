import numpy as np 

#make (3,2,2) array #3 rows , #2coloumn , #2depth
my_matrix = np.array ([[[1,2],[3,4]] , [[5,6],[7,8]] , [[9,10],[11,12]]])
# print(my_matrix)

# ndarray.ndim : the number of axes
print(my_matrix.ndim) 
# ndarray.size : the total number of element
print(my_matrix.size)
#ndarray.shape : the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).
print(my_matrix.shape)