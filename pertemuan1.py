import numpy as np
from numpy import random

#Buat array 1 dimensi yang terdiri dari 5 bilangan bulat random dari 0 sampai 100
x = random.randint(100, size=5)
print(x)

#Buat array 2 dimensi dengan 3 rows dan masing2 row terdiri dari 5 bilangan bulat random dari 0 sampai 100
y = random.randint(100, size=(3,5))
print(y)

#Buat array 1 dimensi diantara bilangan 1.5 dan 5.5 -> (termasuk) yang terdiri dari 30 element
z = np.linspace(1.5,5.5,30)
print(z)