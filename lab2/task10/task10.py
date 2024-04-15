import numpy as np

# 构建特征矩阵
feature_matrix = np.array([
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0]
])

# 定义计算余弦相似度的函数
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

# 计算余弦相似度矩阵
cosine_sim_matrix = np.zeros((feature_matrix.shape[0], feature_matrix.shape[0]))
for i in range(feature_matrix.shape[0]):
    for j in range(feature_matrix.shape[0]):
        cosine_sim_matrix[i, j] = cosine_similarity(feature_matrix[i], feature_matrix[j])

print("Cosine Similarity Matrix:")
print(cosine_sim_matrix)

# 使用SVD分解计算相似度
U, S, Vt = np.linalg.svd(feature_matrix, full_matrices=False)
# 选择前两个最大的奇异值
k = 2
S_k = np.diag(S[:k])
U_k = U[:, :k]
Vt_k = Vt[:k, :]

# 重构特征矩阵
reconstructed_matrix = U_k.dot(S_k).dot(Vt_k)

# 计算相似度矩阵
svd_sim_matrix = np.dot(reconstructed_matrix, reconstructed_matrix.T)

print("\nSVD Similarity Matrix:")
print(svd_sim_matrix)
