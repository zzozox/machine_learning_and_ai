import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score

# 1. 读取数据集并进行数据预处理
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv('dataset/iris.csv', names=column_names)

# 标准化数据
scaler = StandardScaler()
scaled_features = scaler.fit_transform(iris_data.drop('species', axis=1))

# 将类别标签编码为数字
label_encoder = LabelEncoder()
encoded_species = label_encoder.fit_transform(iris_data['species'])

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(scaled_features, encoded_species, test_size=0.3, random_state=42)

# 2. 训练随机森林模型
def train_random_forest():
    rf_classifier = RandomForestClassifier(criterion='entropy', n_estimators=10)
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# 3. 测试随机森林模型的正确率
rf_accuracy = train_random_forest()
print("Accuracy using Random Forest:", rf_accuracy)
print()

# 4. 使用网格搜索确定最优参数
param_grid = {'max_depth': range(1, 6), 'n_estimators': range(1, 21)}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=10)
grid_search.fit(scaled_features, encoded_species)

print("Best max_depth for Random Forest:", grid_search.best_params_['max_depth'])
print("Best n_estimators for Random Forest:", grid_search.best_params_['n_estimators'])
