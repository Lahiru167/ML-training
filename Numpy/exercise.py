import numpy as np

np.random.seed(42)
arr = np.random.randint(1,101, size=(3,4,5))

print("3D Array: \n", arr)
print(arr)

print("Mean axis =0: ",np.mean(arr, axis=0))
print("Mean axis =1: ",np.mean(arr, axis=1))
print("Mean axis =2: ",np.mean(arr, axis=2))

print("Sum axis =0: ",np.sum(arr, axis=0))

    