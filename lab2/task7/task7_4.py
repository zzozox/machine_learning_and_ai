import numpy as np

A1 = np.array([[1,2,3],[4,5,6]])
A2 = np.array([[1,2],[3,4],[5,6]])
x1 = np.array([[1],[2],[3]])
x2 = np.array([1,2,3])
x3 = np.array([1,2])

r1 = A1.dot(A2)
r2 = A1.dot(x1)
r3 = A1.dot(x2)
r4 = A1.dot(x3)
r5 = x2.dot(A1)
r6 = x3.dot(A1)
