import numpy as np

np.random.seed(42)

random_arr = np.random.rand(3,3)
print("Random Array: \n ", random_arr)

random_interger = np.random.randint(1, 10, size=(2,3))
print("Random Integer Array: \n", random_interger)