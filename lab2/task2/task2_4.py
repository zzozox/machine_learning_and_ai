import numpy as np

# 创建原始数组a
a = np.array([1, 2, 3, 4, 5])

# 使数组b与数组a共享同一块数据内存(数组b引用数组a)
b = a
print("Array b referencing array a:")
print("a:", a)
print("b:", b)

# 将数组a的值做一份拷贝后再赋给b，a和b各自保留自己的数据内存
a_copy = np.copy(a)
b = a_copy
print("\nArray b with copied values from array a:")
print("a:", a)
print("b:", b)

# 修改数组a的值，观察数组b的变化
a[0] = 100
print("\nAfter modifying array a:")
print("a:", a)
print("b:", b)
