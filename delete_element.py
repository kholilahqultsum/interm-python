import numpy as np 

my_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])

#menghapus baris ke 3 dalam array
x = np.delete(my_array, 3, axis=0)
print(x)

# menghapus baris sesuai dengan angka yang diinginkan (dapat menulis berapapun)
x = np.delete(my_array,(0,1,3,4), axis=0)
print(x)

#menghapus baris secara urut
x = np.delete(my_array, np.s_[2:], axis=0)
print(x)

#Apabila menghapus kolom, gunakan axis = 1
