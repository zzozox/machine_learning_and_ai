import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score

# 读取数据集并手动添加列名
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
data = pd.read_csv('datasets/iris.csv', names=column_names)

# 准备特征和标签
X = data.drop('species', axis=1)
y = data['species']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化准确率列表
accuracies = []

# 尝试多项式次数为 1-9 的逻辑回归模型
for degree in range(1, 10):
    # 创建多项式特征
    poly_features = PolynomialFeatures(degree=degree)
    X_train_poly = poly_features.fit_transform(X_train)
    X_test_poly = poly_features.transform(X_test)

    # 初始化并拟合逻辑回归模型
    logistic_reg = LogisticRegression(solver='liblinear', multi_class='auto')
    logistic_reg.fit(X_train_poly, y_train)

    # 在测试集上进行预测
    y_pred = logistic_reg.predict(X_test_poly)

    # 计算准确率并添加到列表中
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

    # 打印当前多项式次数下的准确率
    print(f"Degree {degree}: Accuracy = {accuracy}")

# 找出最优多项式次数
best_degree = np.argmax(accuracies) + 1
print(f"The best degree for logistic regression is: {best_degree}")
