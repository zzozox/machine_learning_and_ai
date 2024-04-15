import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier
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

# 2. 训练决策树模型
def train_decision_tree(criterion):
    dt_classifier = DecisionTreeClassifier(criterion=criterion)
    dt_classifier.fit(X_train, y_train)
    y_pred = dt_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# 3. 测试不同特征选择标准的决策树模型的正确率
gini_accuracy = train_decision_tree("gini")
entropy_accuracy = train_decision_tree("entropy")

print("Accuracy using 'gini' criterion:", gini_accuracy)
print("Accuracy using 'entropy' criterion:", entropy_accuracy)
print()

# 4. 使用网格搜索确定最优参数
param_grid = {'max_depth': range(1, 6), 'max_features': range(1, 5)}
grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=10)
grid_search.fit(scaled_features, encoded_species)

print("Best max_depth:", grid_search.best_params_['max_depth'])
print("Best max_features:", grid_search.best_params_['max_features'])
print()

# 5. 使用最优参数重新训练模型
best_max_depth = grid_search.best_params_['max_depth']
best_max_features = grid_search.best_params_['max_features']
best_dt_classifier = DecisionTreeClassifier(max_depth=best_max_depth, max_features=best_max_features)
best_dt_classifier.fit(X_train, y_train)

# 6. 十折交叉验证评估模型
cross_val_scores = cross_val_score(best_dt_classifier, scaled_features, encoded_species, cv=10)
mean_accuracy = cross_val_scores.mean()

print("Average prediction accuracy after using optimal parameters:", mean_accuracy)
