import numpy as np

# 创建具有 10 个元素的全 0 值数组
array1 = np.zeros(10)
print("Array with 10 elements all zeros:")
print(array1)

# 创建 2x3 的全 0 值二维数组
array2 = np.zeros((2, 3))
print("\n2x3 array with all zeros:")
print(array2)

# 创建 2x3 的全 0 值二维整数数组
array3 = np.zeros((2, 3), dtype=int)
print("\n2x3 integer array with all zeros:")
print(array3)

# 创建 2x3 的全 1 值二维数组
array4 = np.ones((2, 3))
print("\n2x3 array with all ones:")
print(array4)

# 创建 2x3 的二维数组，每个元素值都是 5
array5 = np.full((2, 3), 5)
print("\n2x3 array with all elements equal to 5:")
print(array5)

# 创建 3x3 的二维数组，并且主对角线上元素都是 1
array6 = np.eye(3)
print("\n3x3 array with ones on the main diagonal:")
print(array6)

# 创建 mxn 的二维数组，并且主对角线上元素都是 1
m = 4
n = 5
array7 = np.eye(min(m, n))
print(f"\n{m}x{n} array with ones on the main diagonal:")
print(array7)

# 创建 2x3 的二维数组，不指定初始值
array8 = np.empty((2, 3))
print("\n2x3 empty array:")
print(array8)
