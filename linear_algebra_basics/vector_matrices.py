import numpy as np
v = np.array([1,2,3])
v
# OUT: array([1, 2, 3])
v2 = np.array([4,5,6])
v2
# OUT: array([4, 5, 6])
c = v + v2
c
# OUT: array([5, 7, 9])
v3 = np.array([0.5, 0.5, 0.5])
c = v - v3
c
# OUT: array([0.5, 1.5, 2.5])
v*v2
# OUT: array([ 4, 10, 18])
v.dot(v2)
# OUT: 32
v/v3
# OUT: array([2., 4., 6.])
v * 3
# OUT: array([3, 6, 9])
from numpy.linalg import norm
a = np.array([1,2,3])
l1 = norm(a,1)
l1
# OUT: 6.0
l2 = norm(a,2)
l2
# OUT: 3.7416573867739413
from math import inf
maxnorm = norm(a, inf)
maxnorm
# OUT: 3.0
A = np.array([[1,2,3], [4,5,6]])
A
# OUT: array([[1, 2, 3],
# OUT:        [4, 5, 6]])
B = np.array([[3,3,3],[2,2,2]])
B
# OUT: array([[3, 3, 3],
# OUT:        [2, 2, 2]])
A + B
# OUT: array([[4, 5, 6],
# OUT:        [6, 7, 8]])
B - A
# OUT: array([[ 2,  1,  0],
# OUT:        [-2, -3, -4]])
Hadamard_prod = A * B 
Hadamard_prod
# OUT: array([[ 3,  6,  9],
# OUT:        [ 8, 10, 12]])
C = A/B
C
# OUT: array([[0.33333333, 0.66666667, 1.        ],
# OUT:        [2.        , 2.5       , 3.        ]])
C = A.dot(B) #matrix multiplication
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT:     C = A.dot(B) #matrix multiplication
# OUT: ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)

B = np.array([[1,2],[3,4],[5,6]])
C = A.dot(B)
C
# OUT: array([[22, 28],
# OUT:        [49, 64]])
D = A @ B 
D
# OUT: array([[22, 28],
# OUT:        [49, 64]])

A.shape
# OUT: (2, 3)
B = np.array([0.5,0.5,0.5])
A @ B 
# OUT: array([3. , 7.5])
A * 0.5
# OUT: array([[0.5, 1. , 1.5],
# OUT:        [2. , 2.5, 3. ]])