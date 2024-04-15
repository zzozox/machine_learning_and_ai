import numpy as np

# 创建两个二维数组
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# 以竖直方向叠加两个数组
vertical_stack = np.vstack((array1, array2))
print("Vertically stacked arrays:")
print(vertical_stack)

# 以水平方向叠加两个数组
horizontal_stack = np.hstack((array1, array2))
print("\nHorizontally stacked arrays:")
print(horizontal_stack)

# 竖直方向将二维数组拆分成若干个数组
split_vertical = np.vsplit(vertical_stack, 2)
print("\nVertically split arrays:")
for arr in split_vertical:
    print(arr)

# 水平方向将二维数组拆分成若干个数组
split_horizontal = np.hsplit(horizontal_stack, 2)
print("\nHorizontally split arrays:")
for arr in split_horizontal:
    print(arr)
