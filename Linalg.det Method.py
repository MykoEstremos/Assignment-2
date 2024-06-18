# linalg.det method
import numpy as np
from numpy.linalg import det

#EXAMPLE 1
# Define a matrix
A = np.array([[4, 6], [3, 9]])

result = det(A)

print(f'EXAMPLE 1:{result}')

#EXAMPLE 2
B = np.array([[7, 3], [4, 9]])

result = det(B)
print(f'EXAMPLE 2:{result}')

#EXAMPLE 3
C = np.array([[8, 3, 9], [0, 4, 6], [2, 7, 9]])

result = det(C)
print(f'EXAMPLE 3:{result}')