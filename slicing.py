import numpy as np

my_matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(my_matrix)

# #my_matrix[row,coloumn]

# #Hold 11 and 12 only
print(my_matrix[2,2:])

# #Hold 6 and 10 only
print(my_matrix[1:3,1])

#(2,2,3) marix
my_matrix = np.array([[[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]]])
print(my_matrix.shape)

#Acces row 1
print(my_matrix[1])

# #Acces row 0 coloumn 1 
print(my_matrix[0,0])

#Acces row 1, coloumn 1, depth 1
print(my_matrix[1,1,1])

#Acces row 0, coloumn 0 & 1, depth 1 & 2
print(my_matrix[0,0:,1:])