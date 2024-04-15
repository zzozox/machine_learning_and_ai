import numpy as np

# 创建行向量数组
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 3, 2, 1])

# 各元素分别计算 x1 * 5 + 2
result1 = x1 * 5 + 2
print("Result of x1 * 5 + 2:")
print(result1)

# 对应元素分别相乘
result2 = x1 * x2
print("\nResult of element-wise multiplication:")
print(result2)
