import numpy as np
M = np.array([[1,2,3],[1,2,3],[1,2,3]])
M
# OUT: array([[1, 2, 3],
# OUT:        [1, 2, 3],
# OUT:        [1, 2, 3]])
np.tril(M)
# OUT: array([[1, 0, 0],
# OUT:        [1, 2, 0],
# OUT:        [1, 2, 3]])
np.triu(M)
# OUT: array([[1, 2, 3],
# OUT:        [0, 2, 3],
# OUT:        [0, 0, 3]])
np.diag(M)
# OUT: array([1, 2, 3])
d = np.diag(M)
D = np.diag(d)
D
# OUT: array([[1, 0, 0],
# OUT:        [0, 2, 0],
# OUT:        [0, 0, 3]])
I = np.identity(3)
I
# OUT: array([[1., 0., 0.],
# OUT:        [0., 1., 0.],
# OUT:        [0., 0., 1.]])
from numpy.linalg import inv 
Q = np.array([[1,0],[0,-1]])
Q
# OUT: array([[ 1,  0],
# OUT:        [ 0, -1]])
V = inv(Q)
V
# OUT: array([[ 1.,  0.],
# OUT:        [-0., -1.]])
Q.T
# OUT: array([[ 1,  0],
# OUT:        [ 0, -1]])
Q.dot(V)
# OUT: array([[1., 0.],
# OUT:        [0., 1.]])
A = np.array([[1,2],[3,4],[5,6]])
A
# OUT: array([[1, 2],
# OUT:        [3, 4],
# OUT:        [5, 6]])
A.T
# OUT: array([[1, 3, 5],
# OUT:        [2, 4, 6]])
A = np.array([[1,2],[3,4]])
A
# OUT: array([[1, 2],
# OUT:        [3, 4]])
B = inv(A)
B
# OUT: array([[-2. ,  1. ],
# OUT:        [ 1.5, -0.5]])
A.dot(B)
# OUT: array([[1.0000000e+00, 0.0000000e+00],
# OUT:        [8.8817842e-16, 1.0000000e+00]])
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
A
# OUT: array([[1, 2, 3],
# OUT:        [4, 5, 6],
# OUT:        [7, 8, 9]])
np.trace(A)
# OUT: 15
from numpy.linalg import det 
det(A)
# OUT: 0.0
from numpy.linalg import matrix_rank
v1 = np.array([1,2,3])
v1_rank = matrix_rank(v1)
v1_rank 
# OUT: 1
M0 = np.array([[0,0],[0,0]])
matrix_rank(M0)
# OUT: 0
M1 = np.array([[1,2],[1,2]])
matrix_rank(M1)
# OUT: 1
M2 = np.array([[1,2],[3,4]])
matrix_rank(M2)
# OUT: 2