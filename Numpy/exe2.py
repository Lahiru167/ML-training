import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('original matrix\n',matrix)

transposed = matrix.T
print('transposed matrix\n',transposed)


matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print('original matrix\n',matrix2)

print('matrix addition\n',matrix + matrix2)
print('matrix subtraction\n',matrix - matrix2)
print('matrix multiplication\n',matrix * matrix2)
