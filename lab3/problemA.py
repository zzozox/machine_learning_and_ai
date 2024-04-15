import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# 1. 读取数据集并画出散点图
data = pd.read_csv('datasets/Advertising.csv')
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

plt.figure(figsize=(10, 8))
plt.scatter(data['TV'], y, marker='o', label='TV')
plt.scatter(data['Radio'], y, marker='s', label='Radio')
plt.scatter(data['Newspaper'], y, marker='^', label='Newspaper')
plt.xlabel('Advertising Cost')
plt.ylabel('Sales')
plt.grid(True, linestyle='--')
plt.legend()
plt.title('Advertising Cost vs Sales')
plt.show()

# 保存第一张图
plt.savefig(os.path.join('output', 'scatter_plot_all.png'))

# 2. 分别画出TV、Radio、Newspaper与Sales的散点图
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

axes[0].scatter(data['TV'], y)
axes[0].set_title('TV vs Sales')
axes[0].set_xlabel('TV Advertising Cost')
axes[0].set_ylabel('Sales')
axes[0].grid(True, linestyle='--')

axes[1].scatter(data['Radio'], y)
axes[1].set_title('Radio vs Sales')
axes[1].set_xlabel('Radio Advertising Cost')
axes[1].set_ylabel('Sales')
axes[1].grid(True, linestyle='--')

axes[2].scatter(data['Newspaper'], y)
axes[2].set_title('Newspaper vs Sales')
axes[2].set_xlabel('Newspaper Advertising Cost')
axes[2].set_ylabel('Sales')
axes[2].grid(True, linestyle='--')

plt.tight_layout()
plt.show()

# 保存第二张图
plt.savefig(os.path.join('output', 'scatter_plots_separate.png'))

# 3. 多项式拟合模型
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

train_errors = []
test_errors = []
degrees = range(1, 10)

plt.figure(figsize=(15, 10))

for i in degrees:
    poly_features = PolynomialFeatures(degree=i)
    X_train_poly = poly_features.fit_transform(X_train)
    X_test_poly = poly_features.transform(X_test)

    lin_reg = LinearRegression()
    lin_reg.fit(X_train_poly, y_train)

    train_pred = lin_reg.predict(X_train_poly)
    test_pred = lin_reg.predict(X_test_poly)

    train_errors.append(mean_squared_error(y_train, train_pred))
    test_errors.append(mean_squared_error(y_test, test_pred))

    plt.subplot(3, 3, i)
    plt.scatter(range(len(y_test)), y_test, color='red', label='Actual Sales')
    plt.plot(range(len(y_test)), test_pred, color='green', label='Predicted Sales')
    plt.title('Degree ' + str(i))
    plt.xlabel('Sample Index')
    plt.ylabel('Sales')
    plt.legend()

plt.tight_layout()
plt.show()

# 保存多项式拟合模型的图
plt.savefig(os.path.join('output', 'polynomial_regression.png'))

best_degree = np.argmin(test_errors) + 1
print(f"The best degree for polynomial regression is: {best_degree}")
