import numpy as np

# 定义矩阵 A1
A1 = np.array([[2, 2, 3], [1, -1, 0], [-1, 2, 1]])

# 计算矩阵 A1 的转置
A1_transpose = np.transpose(A1)
# 或者可以使用 A1.T
# A1_transpose = A1.T

print("Transpose of matrix A1:")
print(A1_transpose)
