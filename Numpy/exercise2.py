import numpy as np

dataset = np.random.randint(1,51, size=(5,5))
print("original Dataset: \n", dataset)

#filter values > 25 and replace them with 0
dataset[dataset > 25] = 0
print("Modified Dataset: \n", dataset)

#calculate summry stats
print("Sum: ", np.sum(dataset))
print("Mean: ",np.mean(dataset))
print("Max: ",np.max(dataset))
print("Min: ",np.min(dataset))
print("Standard Deviation: ",np.std(dataset))