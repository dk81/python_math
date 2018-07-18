# Numpy Work With Linear Algebra
# dk81 Github User

# References: Python For Data Analysis
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

import numpy as np

## Vectors:

a = np.array([1, -1, 2])
b = np.array([2, -1, 3])

print(a)
print(b)

print(a + b) # Vector addition
print(a - b) # Vector subtraction

print(5*a) # Scalar multiplication on vector

# Dot Product (Element wise multiplication and take sum of products):

print(np.dot(a, b)) # (1*2) + (-1)(-1) + 2*3 = 2 + 1 + 6 = 9

# Cross Product (A Vector That Is Perpendicular/Orthogonal To Vectors a and b):

cross_vect = np.cross(a, b)
print(cross_vect)

# Check orthognality by seeing dot product is zero between cross product with a and b:

print(np.dot(cross_vect, a))

print(np.dot(cross_vect, b))

# Function example:

x = np.array([0, 1, 2, 3])

print(np.exp(x))

# Vector with random numbers from a normal distribution.

print(np.random.normal(size = (1, 4)))

#--------------------------------
## Matrices:

# 5 by 5 Identity Matrix

identity_five = np.identity(5)

print(identity_five)

# 3 by 3 Matrix of zeroes:

print(np.zeros( (3, 3)))

# 3 by 3 Matrix of ones:

print(np.ones( (3, 3)))

# Creating a matrix:

A = np.array([[1., 5., 2.], [2., 3.,-1.], [0., 1., -5.]])

print(A)

# Matrix determinant:

det_A = np.linalg.det(A)

print(det_A)


# Diagonal of Matrix:

print(np.diag(A))


# Trace Of A Matrix:

print(np.trace(A))



# Transpose Of Matrix:

print(np.transpose(A)) # Transpose of matrix A

# Inverse Of A Square Matrix:

print(np.linalg.inv(A))

# Eigenvalues and Eigenvectors Of A Square Matrix:

# print(np.linalg.eig(A))

#----------



# Matrix multiplication:

B = np.array([[1, 3], [1, 2]]) # 2 by 2 matrix

D = np.array([[2], [-1]]) # 2 by 1 matrix

print(np.matmul(B, D))

# Solving a linear system example Bx = c.

B = np.array([[1, 3], [1, 2]])

c = np.array([[2], [0]])

print(np.linalg.solve(B, c))


