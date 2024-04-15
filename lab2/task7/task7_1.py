import numpy as np

# 创建矩阵
matrix1 = np.mat([[2, 3, 4], [5, 8, 2]])
vector = np.mat([2, 1, 6])

# 计算矩阵与向量的乘积
result_vector = matrix1 * vector.T  # 使用.T进行向量的转置
print("Matrix-vector product:")
print(result_vector)

# 创建第二个矩阵
matrix2 = np.mat([[2, 3, 4], [5, 8, 2]])
matrix3 = np.mat([[21], [1], [6]])

# 计算矩阵与矩阵的乘积
result_matrix = matrix2 * matrix3
print("\nMatrix-matrix product:")
print(result_matrix)
