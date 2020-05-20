from numpy import empty

a = empty([3,3])
a
# OUT: array([[2.68156159e+154, 2.68678699e+154, 2.13394368e-314],
# OUT:        [2.12768049e-314, 2.13429734e-314, 2.12717793e-314],
# OUT:        [2.12835410e-314, 2.12836343e-314, 2.13419932e-314]])
import numpy as np 
a = np.zeros([3,5])
a
# OUT: array([[0., 0., 0., 0., 0.],
# OUT:        [0., 0., 0., 0., 0.],
# OUT:        [0., 0., 0., 0., 0.]])
np.ones([5])
# OUT: array([1., 1., 1., 1., 1.])
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a3 = np.vstack((a1, a2))
a3
# OUT: array([[1, 2, 3],
# OUT:        [4, 5, 6]])
a4 = np.hstack((a1, a2))
a4
# OUT: array([1, 2, 3, 4, 5, 6])
data = [11,22,33,44,55]
data = np.array(data)
type(data)
# OUT: <class 'numpy.ndarray'>
data
# OUT: array([11, 22, 33, 44, 55])
data = [[11, 22],
[33, 44],
[55, 66]]
data = np.array(data)
data
# OUT: array([[11, 22],
# OUT:        [33, 44],
# OUT:        [55, 66]])
data[0]
# OUT: array([11, 22])
data[2]
# OUT: array([55, 66])
data[-1]
# OUT: array([55, 66])
data[-2]
# OUT: array([33, 44])
data[0][0]
# OUT: 11
data[0,0]
# OUT: 11
data[0,]
# OUT: array([11, 22])
data[,1]
# OUT:   File "<input>", line 1
# OUT:     data[,1]
# OUT:          ^
# OUT: SyntaxError: invalid syntax
data[:,1]
# OUT: array([22, 44, 66])
data[:,0]
# OUT: array([11, 33, 55])
data = np.array([[11,22,33],[44,55,66], [77,88,99]])
X, y = data[:, :-1], data[:, -1]
X
# OUT: array([[11, 22],
# OUT:        [44, 55],
# OUT:        [77, 88]])
y
# OUT: array([33, 66, 99])
train, test = data[:2, :], data[2:, :]
train 
# OUT: array([[11, 22, 33],
# OUT:        [44, 55, 66]])
test 
# OUT: array([[77, 88, 99]])
data = np.array([11, 22, 33, 44, 55])
data.shape
# OUT: (5,)
data = data.reshape((data.shape[0],1))
data
# OUT: array([[11],
# OUT:        [22],
# OUT:        [33],
# OUT:        [44],
# OUT:        [55]])
data = [[11, 22],
[33, 44],
[55, 66]]
data = np.array(data)
data
# OUT: array([[11, 22],
# OUT:        [33, 44],
# OUT:        [55, 66]])
data.shape
# OUT: (3, 2)
data = data.reshape((data.shape[0], data.shape[1], 1))
data
# OUT: array([[[11],
# OUT:         [22]],
# OUT:        [[33],
# OUT:         [44]],
# OUT:        [[55],
# OUT:         [66]]])
data.shape
# OUT: (3, 2, 1)
a = [1,2,3]
b = [3,4,5]
c = a+b
c
# OUT: [1, 2, 3, 3, 4, 5]
a = np.array(a)
b = np.array(b)
a
# OUT: array([1, 2, 3])
b
# OUT: array([3, 4, 5])
c = a+b
c
# OUT: array([4, 6, 8])
a = np.array([1,2,3])
a
# OUT: array([1, 2, 3])
b = 2
c = a+b
c
# OUT: array([3, 4, 5])
A = np.array([[1, 2, 3],[1,2,3]])
A
# OUT: array([[1, 2, 3],
# OUT:        [1, 2, 3]])
b = 2 
C = A + b
C
# OUT: array([[3, 4, 5],
# OUT:        [3, 4, 5]])
b = np.array([1,2,3])
C = A + b
C
# OUT: array([[2, 4, 6],
# OUT:        [2, 4, 6]])
A.shape
# OUT: (2, 3)
b.shape
# OUT: (3,)
b = np.array([1,2])
A + b 
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT:     A + b
# OUT: ValueError: operands could not be broadcast together with shapes (2,3) (2,) 