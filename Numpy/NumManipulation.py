import numpy as np

arr = np.array([1, 2, 3, 4, 5,6,7,8,9])

reshaped= arr.reshape(3,3)
print(reshaped)

arr1 = np.array([1,2,3])
expanded = arr1[:,np.newaxis]
print(expanded)