import numpy as np

# 一维数组中，查找不为 0 的元素
array_1d = np.array([1, 0, 3, 0, 5])
non_zero_elements_1d = array_1d[array_1d != 0]
print("Non-zero elements in 1D array:", non_zero_elements_1d)

# 二维数组中，查找不为 0 的元素
array_2d = np.array([[1, 0, 3], [0, 5, 0], [7, 0, 9]])
non_zero_elements_2d = array_2d[array_2d != 0]
print("\nNon-zero elements in 2D array:")
print(non_zero_elements_2d)

# 查找指定条件的元素
specified_condition_elements = array_1d[array_1d > 2]
print("\nElements greater than 2 in 1D array:", specified_condition_elements)

# 返回条件为 True 的元素
condition = array_1d > 2
true_elements = array_1d[condition]
print("\nElements with condition True in 1D array:", true_elements)

# 返回指定索引的若干个元素
specified_indices_elements = array_1d[[0, 2, 4]]
print("\nElements at specified indices in 1D array:", specified_indices_elements)
