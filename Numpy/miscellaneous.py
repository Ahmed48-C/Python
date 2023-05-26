import numpy as np


data = np.genfromtxt(r'C:/Users/Karim/Desktop/Python/Numpy/data.txt', delimiter=',', )
print(data)
data = data[~np.isnan(data)]
print(data)
print(data.astype('int32'))

# Boolean Masking And Advanced Indexing

print(data > 50)
print(data[data > 50])
print(np.any(data > 50, axis=0))
print(np.all(data > 50, axis=0))

a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

