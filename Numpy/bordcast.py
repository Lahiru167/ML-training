import numpy as np

# array and Scalar  bordcasting
arr =np. array([1, 2, 3])

print(arr+10)


matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
print(matrix + vector)


arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print("sum: ", np.sum(arr1))
print("Mean: ",np,np.mean(arr1))
print("Max: ",np.max(arr1))
print("Min: ",np.min(arr1))
print("Standard Deviation: ",np.std(arr1))
print("Sum along  rows: ",np.sum(arr1, axis=1))
print("Sum along columns: ",np.sum(arr1, axis=0))