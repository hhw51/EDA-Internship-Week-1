import numpy as np

arr = np.random.rand(3, 4)
mean = np.mean(arr, axis=1)
dev = np.std(arr, axis=1)
var = np.var(arr, axis=1)

print("Mean along second axis:", mean)
print("Standard deviation along second axis:", dev)
print("Variance along second axis:", var)