import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))
print(arr[0:3])

arr2 = np.array([
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 9]
])

print(arr2[0:2, 0:2])
print(np.shape(arr2))
print(arr2.dtype)