import numpy as np

# 定义矩阵 A1
A1 = np.array([[2, 1, 3], [6, 6, 10], [2, 7, 6]])

# 计算矩阵 A1 的秩
rank_A1 = np.linalg.matrix_rank(A1)
print("Rank of matrix A1:", rank_A1)

# 定义矩阵 A2
A2 = np.array([[2, 1, 3], [4, 2, 6], [2, 7, 6]])

# 计算矩阵 A2 的秩
rank_A2 = np.linalg.matrix_rank(A2)
print("Rank of matrix A2:", rank_A2)

# 定义矩阵 A3
A3 = np.array([[2, 1, 3], [6, 6, 10], [2, 7, 6], [1, 3, 5]])

# 计算矩阵 A3 的秩
rank_A3 = np.linalg.matrix_rank(A3)
print("Rank of matrix A3:", rank_A3)
