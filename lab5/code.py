import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# 读取数据
data = pd.read_csv('dataset/Advertising.csv')

# 特征选择
X = data.drop(columns=['Sales'])
y = data['Sales']

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 使用回归树
reg_tree = DecisionTreeRegressor()
reg_tree.fit(X_train, y_train)
y_pred_tree = reg_tree.predict(X_test)
mse_tree = mean_squared_error(y_test, y_pred_tree)

# 使用线性回归
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)
mse_lin = mean_squared_error(y_test, y_pred_lin)

# 使用XGBoost回归
xgb_reg = XGBRegressor()
param_grid = {'n_estimators': range(100, 1001, 100)}
grid_search = GridSearchCV(estimator=xgb_reg, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
best_n_estimators = best_params['n_estimators']

xgb_reg_best = XGBRegressor(n_estimators=best_n_estimators)
xgb_reg_best.fit(X_train, y_train)
y_pred_xgb = xgb_reg_best.predict(X_test)
mse_xgb = mean_squared_error(y_test, y_pred_xgb)

print("Mean Squared Error (MSE) - Decision Tree: {:.2f}".format(mse_tree))
print("Mean Squared Error (MSE) - Linear Regression: {:.2f}".format(mse_lin))
print("Mean Squared Error (MSE) - XGBoost: {:.2f}".format(mse_xgb))
