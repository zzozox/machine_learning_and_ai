import numpy as np

# 定义矩阵 A1
A1 = np.array([[2, 2, 3], [1, -1, 0], [-1, 2, 1]])

# 计算矩阵 A1 的逆
A1_inverse = np.linalg.inv(A1)

print("Inverse of matrix A1:")
print(A1_inverse)
