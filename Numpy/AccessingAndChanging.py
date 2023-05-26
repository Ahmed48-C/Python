# Accessing/Changing specific elements, rows, columns, etc
import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]]) #2D array, 2 by 7 array

# Get specific element [r, c]
print(a[1,5]) #This prints 13 because rows and columns start from 0 not 1

# Get specific row
print(a[0])
# or you can do:
print(a[0, :])

# Get specific column
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2]) # printing 2,4,6

# Changing elements in arrays
a[1,5] = 20
a[:,2] = [1,2]
print(a)

# 3D example
b = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(b)

# Get specific element (work outside in)
print(b[0,1,1])
print(b[:,1,:])