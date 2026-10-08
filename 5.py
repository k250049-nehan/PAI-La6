import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print("Shape of A:",A.shape)
print("Shape of B:",B.shape)

print("\nAddition:")
print(A+B)

print("\nSubtraction:")
print(A-B)

print("\nElement-wise Multiplication:")
print(A*B)

print("\nMatrix Multiplication:")
print(A@B)

print("\nTranspose of A:")
print(A.T)

print("\nDeterminant of A:")
print(np.linalg.det(A))

print("\nInverse of A:")
print(np.linalg.inv(A))
