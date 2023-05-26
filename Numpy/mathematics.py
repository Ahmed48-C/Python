import numpy as np

a = np.array([1,2,3,4])
print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)

b = np.array([1,0,1,0])
print(a + b)

print(np.sin(a))
print(np.tan(a))
print(np.cos(a))
print(np.log(a))


# Linear Algebra
a = np.ones((2,3))
b = np.full((3,2), 2)
print(a)
print(b)
print(np.matmul(a,b))

# Find the determinant
c = np.identity(3)
print(c)
print(np.linalg.det(c))