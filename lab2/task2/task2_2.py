import numpy as np

# 创建 5 个元素的一维数组，初始化为 1,2,3,4,5
array1d = np.array([1, 2, 3, 4, 5])
print("One-dimensional array initialized with values 1, 2, 3, 4, 5:")
print(array1d)

# 创建 2x3 的二维数组，用指定的元素值初始化
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTwo-dimensional array initialized with specified values:")
print(array2d)

# a 是 mxn 数组，根据 a 的维度生成 mxn 的全 0 值数组 b
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.zeros_like(a)
print("\nArray b with same shape as a initialized with zeros:")
print(b)

# 以指定的主对角线元素创建对角矩阵
diagonal_values = [1, 2, 3]
diagonal_matrix = np.diag(diagonal_values)
print("\nDiagonal matrix with specified diagonal elements:")
print(diagonal_matrix)
