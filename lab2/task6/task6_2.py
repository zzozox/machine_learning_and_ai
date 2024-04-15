import numpy as np

# 直接创建列向量
column_vector = np.array([[1], [2], [3], [4], [5]])
print("Column vector:")
print(column_vector)

# 将列向量转成 1xm 的行向量
row_vector = column_vector.flatten()
print("\nRow vector (1xm):")
print(row_vector)

# 将一个一维数组转成列向量
array_1d = np.array([1, 2, 3, 4, 5])
column_vector_from_array = array_1d[:, np.newaxis]
print("\nColumn vector from 1D array:")
print(column_vector_from_array)

# 借助 mat 类，然后通过转置实现列向量
column_vector_mat = np.mat(array_1d)
column_vector_transposed = column_vector_mat.T
print("\nColumn vector using mat class and transpose:")
print(column_vector_transposed)

# 使用 reshape 方法, 将原来的一维数组变成了 mx1 形式的二维数组
reshaped_column_vector = array_1d.reshape(-1, 1)
print("\nReshaped column vector:")
print(reshaped_column_vector)
