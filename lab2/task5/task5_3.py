import numpy as np

# 查找一维数组中的最大、最小值
array_1d = np.array([3, 1, 4, 1, 5])
max_value_1d = np.max(array_1d)
min_value_1d = np.min(array_1d)
print("Max value in 1D array:", max_value_1d)
print("Min value in 1D array:", min_value_1d)

# 查找二维数组总的最大、最小值
array_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
max_value_2d = np.max(array_2d)
min_value_2d = np.min(array_2d)
print("\nMax value in 2D array:", max_value_2d)
print("Min value in 2D array:", min_value_2d)

# 查找极值元素的索引
max_index_1d = np.argmax(array_1d)
min_index_1d = np.argmin(array_1d)
print("\nIndex of max value in 1D array:", max_index_1d)
print("Index of min value in 1D array:", min_index_1d)

# 统计数组中非零元素个数
count_nonzero = np.count_nonzero(array_1d)
print("\nNumber of nonzero elements in 1D array:", count_nonzero)

# 计算数组算数平均值
mean_value = np.mean(array_1d)
print("\nArithmetic mean of 1D array:", mean_value)

# 计算数组的加权平均值
weights = np.array([1, 2, 3, 4, 5])
weighted_mean = np.average(array_1d, weights=weights)
print("\nWeighted mean of 1D array:", weighted_mean)
