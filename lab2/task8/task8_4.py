import numpy as np

# 定义矩阵 A1
A1 = np.array([[2, 2, 3], [1, -1, 0], [-1, 2, 1]])

# 计算矩阵 A1 的奇异值分解
U1, S1, V1 = np.linalg.svd(A1)

print("Singular value decomposition of matrix A1:")
print("U1:")
print(U1)
print("\nS1:")
print(np.diag(S1))
print("\nV1:")
print(V1)

# 定义矩阵 A2
A2 = np.array([[2, 2, 3], [4, 4, 6], [-1, 2, 1]])

# 计算矩阵 A2 的奇异值分解
U2, S2, V2 = np.linalg.svd(A2)

print("\nSingular value decomposition of matrix A2:")
print("U2:")
print(U2)
print("\nS2:")
print(np.diag(S2))
print("\nV2:")
print(V2)

# 定义矩阵 A3
A3 = np.array([[2, 2, 3], [1, -1, 0], [-1, 2, 1], [-3, 1, 2]])

# 计算矩阵 A3 的奇异值分解
U3, S3, V3 = np.linalg.svd(A3)

print("\nSingular value decomposition of matrix A3:")
print("U3:")
print(U3)
print("\nS3:")
print(np.diag(S3))
print("\nV3:")
print(V3)
