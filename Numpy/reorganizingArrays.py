import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before.shape)

after = before.reshape((4,2))
after2 = before.reshape((2,2,2))

print(after)
print(after2)


# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v2,v1]))

# Horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack([h1,h2]))
print(np.hstack([h1,h2,h1]))