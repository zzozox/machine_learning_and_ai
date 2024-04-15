import numpy as np

# 将数组倒序
array_reverse = np.array([3, 1, 4, 1, 5])
array_reverse_sorted = np.flip(array_reverse)
print("Reversed array:", array_reverse_sorted)

# 一维数组排序
array_1d = np.array([3, 1, 4, 1, 5])
array_1d_sorted = np.sort(array_1d)
print("\nSorted 1D array:", array_1d_sorted)

# 二维数组排序
array_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
array_2d_sorted = np.sort(array_2d, axis=None)
print("\nSorted flattened 2D array:", array_2d_sorted)

# 以指定索引位置作为分界线排序
array_partition = np.array([3, 1, 4, 1, 5])
partition_index = 2  # 以索引2处的元素作为分界线
partitioned_array = np.partition(array_partition, partition_index)
print("\nPartitioned array with partition index as boundary:")
print(partitioned_array)
