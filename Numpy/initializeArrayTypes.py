import numpy as np

# All 0s matrix
print(np.zeros(5))
print(np.zeros((2,3)))
print(np.zeros(((2,3,3))))

# All 1s matrix
print(np.ones((4,2,2)))

# Any other number
print(np.full((2,2), 99))

# Any other number (full_like)
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.full_like(a, 4))

# Random decimal number (between 0,1)
print(np.random.rand(4,2))
print(np.random.rand(4,2,3))
print(np.random.random_sample(a.shape))

# Random integer value
print(np.random.randint(1,7, size=(3,3)))

# The identity matrix
print(np.identity(5)) #square

# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)


output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:-1,1:-1] = z
print(output)