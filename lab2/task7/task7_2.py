import numpy as np

# 创建矩阵和向量（列向量、行向量）
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
column_vector = np.array([[1], [2], [3]])
row_vector = np.array([1, 2, 3])

print("Matrix:")
print(matrix)
print("\nColumn vector:")
print(column_vector)
print("\nRow vector:")
print(row_vector)

# 生成特殊矩阵
zeros_matrix = np.zeros((2, 3))
ones_matrix = np.ones([2, 3])
identity_matrix = np.identity(3)
diagonal_matrix = np.diag([1, 2, 3, 4])

print("\nZeros matrix (2x3):")
print(zeros_matrix)
print("\nOnes matrix (2x3):")
print(ones_matrix)
print("\nIdentity matrix (3x3):")
print(identity_matrix)
print("\nDiagonal matrix:")
print(diagonal_matrix)
