import numpy as np

# 定义矩阵 A
A = np.array([[2, 2, 3], [1, -1, 0], [-1, 2, 1]])

# 计算矩阵 A 的特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues of matrix A:")
print(eigenvalues)

print("\nEigenvectors of matrix A:")
print(eigenvectors)
