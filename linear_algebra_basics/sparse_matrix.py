import numpy as np
from scipy.sparse import csr_matrix
A = np.array([[1,0,0,1,0,0],[0,0,2,0,0,1],[0,0,0,2,0,0]])
A
# OUT: array([[1, 0, 0, 1, 0, 0],
# OUT:        [0, 0, 2, 0, 0, 1],
# OUT:        [0, 0, 0, 2, 0, 0]])
S = csr_matrix(A)
S
# OUT: <3x6 sparse matrix of type '<class 'numpy.longlong'>'
# OUT: 	with 5 stored elements in Compressed Sparse Row format>

B = S.todense()
B
# OUT: matrix([[1, 0, 0, 1, 0, 0],
# OUT:         [0, 0, 2, 0, 0, 1],
# OUT:         [0, 0, 0, 2, 0, 0]], dtype=int64)
A.size
# OUT: 18
sparsity = 1 - np.count_nonzero(A)/A.size
sparsity
# OUT: 0.7222222222222222