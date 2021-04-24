import numpy as np
my_matrix = np.arange(10)
#menghasilkan matrix 1D dengan 6 kolom
print(my_matrix)

#reshape ke matrix 2D
print(my_matrix.reshape(2,5))
print(my_matrix.reshape(5,2))