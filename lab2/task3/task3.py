import numpy as np
import matplotlib.pyplot as plt

# 生成网格数据点
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 3)
X, Y = np.meshgrid(x, y)

# 输出网格数据点
print("X (grid points along horizontal direction):")
print(X)
print("\nY (grid points along vertical direction):")
print(Y)

# 绘制网格数据点
plt.scatter(X, Y, color='blue', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grid Points')
plt.grid(True)
plt.show()
