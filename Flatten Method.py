#FLATTEN METHOD
import numpy as np

#EXAMPLE 1
array = np.array([[4, 2, 7], [6, 1, 9]])

result = array.flatten()
print(f'EXAMPLE 1:{result}')

#EXAMPLE 2

array2 = np.array([[[7, 9], [3, 2]], [[4, 9], [7, 8]]])

result = array.flatten()
print(f'EXAMPLE 2:{result}')

#EXAMPLE 3

x = np.array([[5, 2], [3, 9]])
y = np.array([[7, 6], [3, 8]])

z = np.dot(x, y)

result = z.flatten()
print(f'EXAMPLE 3:{result}')