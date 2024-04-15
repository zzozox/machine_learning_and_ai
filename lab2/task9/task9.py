import numpy as np

# 系数矩阵 A
A = np.array([[2, 1, 3], [6, 6, 10], [2, 7, 6]])

# 常数向量 b
b = np.array([2, 7, 6])

# 求解线性方程组
solution = np.linalg.solve(A, b)

print("Solution to the linear equation system:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
