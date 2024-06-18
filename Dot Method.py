#DOT METHOD
import numpy as np

#EXAMPLE 1
x = np.array([[2.5, 3.7], [4.9, 5.1]])
y = np.array([[1, 2], [3, 4]])

result = np.dot(x,y)

print(f'EXAMPLE 2:{result}')

#EXAMPLE 2
x2 = np.array([[1, 2], [3, 4]])
y2 = np.array([[5, 6], [7, 8]])

result = np.dot(x2, y2)

print(f"Example 2: {result}")

#EXAMPLE 3
x3 = np.array([[1, 2], [3, 4]])
y3 = np.array([5, 6])

result = np.dot(x3, y3)

print(f"Example 3: {result}")