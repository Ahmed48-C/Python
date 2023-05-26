import numpy as np

stats = np.array([[1,2,3],[4,5,6]])

print(np.min(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))

print(np.max(stats))
print(np.max(stats, axis=0))
print(np.max(stats, axis=1))

print(np.sum(stats))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))
