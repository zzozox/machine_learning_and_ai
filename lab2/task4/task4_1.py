import numpy as np

# 使用单一值创建数组
single_value_array = np.array([1])

# 查看数组的维度尺寸
print("Array dimension and shape:")
print("Dimension:", single_value_array.ndim)
print("Shape:", single_value_array.shape)

# 将一维数组变形为 mxn 二维数组
m = 1  # 因为数组只包含一个元素，所以只能是1x1的二维数组
n = 1
reshaped_array = single_value_array.reshape(m, n)
print("\nReshaped array to {}x{} matrix:".format(m, n))
print(reshaped_array)

# 将二维数组调整为一行或一列
flattened_row_array = reshaped_array.flatten()
flattened_col_array = reshaped_array.flatten(order='F')  # Column-major order
print("\nFlattened row array:")
print(flattened_row_array)
print("\nFlattened column array:")
print(flattened_col_array)

# 行数组转成列数组
row_to_col_array = single_value_array[:, np.newaxis]
print("\nArray converted from row to column:")
print(row_to_col_array)

# 二维数组展成连续的一维数组
flattened_array = reshaped_array.ravel()
print("\nFlattened array (ravel):")
print(flattened_array)

# 二维数组展成连续的一维数组(拷贝)
flattened_array_copy = reshaped_array.flatten()
print("\nFlattened array (flatten with copy):")
print(flattened_array_copy)

# 将原有数组调整为新指定尺寸的数组(拷贝)
new_shape = (1, 1)
array_reshaped_copy = single_value_array.reshape(new_shape)
print("\nArray reshaped to new shape {} with copy:".format(new_shape))
print(array_reshaped_copy)

# 生成转置数组(矩阵)
transposed_array = reshaped_array.T
print("\nTransposed array (matrix):")
print(transposed_array)
