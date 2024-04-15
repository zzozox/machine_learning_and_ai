import numpy as np

# 创建一个二维数组
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 访问二维数组
print("Accessing elements of the 2D array:")
print(array_2d)

# 访问一维数组的部分元素
array_1d = np.array([1, 2, 3, 4, 5])
partial_array_1d = array_1d[1:4]
print("\nAccessing part of the 1D array:")
print(partial_array_1d)

# 访问二维数组的部分元素
partial_array_2d = array_2d[0:2, 1:3]
print("\nAccessing part of the 2D array:")
print(partial_array_2d)

# 删除元素
array_removed = np.delete(array_1d, 2)
print("\nArray after removing element at index 2:")
print(array_removed)

# 删除行或列
array_removed_row = np.delete(array_2d, 1, axis=0)  # 删除第二行
array_removed_col = np.delete(array_2d, 1, axis=1)  # 删除第二列
print("\nArray after removing a row:")
print(array_removed_row)
print("\nArray after removing a column:")
print(array_removed_col)

# 插入元素、行或列
array_inserted = np.insert(array_1d, 2, 10)  # 在索引2处插入元素10
print("\nArray after inserting element at index 2:")
print(array_inserted)

array_inserted_row = np.insert(array_2d, 1, [10, 11, 12], axis=0)  # 在第二行插入行[10, 11, 12]
print("\nArray after inserting a row:")
print(array_inserted_row)

array_inserted_col = np.insert(array_2d, 1, 10, axis=1)  # 在第二列插入元素10
print("\nArray after inserting a column:")
print(array_inserted_col)

# 追加元素、行或列
array_appended = np.append(array_1d, 6)  # 在末尾追加元素6
print("\nArray after appending element:")
print(array_appended)

array_appended_row = np.append(array_2d, [[10, 11, 12]], axis=0)  # 在末尾追加行[10, 11, 12]
print("\nArray after appending a row:")
print(array_appended_row)

array_appended_col = np.append(array_2d, [[10], [11], [12]], axis=1)  # 在末尾追加列[10, 11, 12]
print("\nArray after appending a column:")
print(array_appended_col)

# 在一个二维数组后添加一列
array_added_column = np.hstack((array_2d, np.array([[10], [11], [12]])))
print("\nArray after adding a column:")
print(array_added_column)
