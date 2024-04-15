import numpy as np

# 根据指定的间距，在[m,n)区间等距切分成若干个数据点，形成数组
def split_range_with_step(m, n, step):
    return np.arange(m, n, step)

# 根据指定的切分点数量，在[m,n]区间等距切分成若干个数据点，形成数组
def split_range_with_count(m, n, count):
    return np.linspace(m, n, count)

# 生成指数间隔的数组
def generate_exponential_array(start, stop, num, base=10.0):
    return np.logspace(start, stop, num=num, base=base)

# 生成网格数据点
def generate_grid_points(x_range, y_range):
    return np.meshgrid(x_range, y_range)

# 测试代码
# 将指定数值范围切分成若干份，形成数组
print("Splitting range [0, 10) into 5 parts:")
print(split_range_with_step(0, 10, 2))

# 根据指定的间距，在[0, 10)区间等距切分成若干个数据点，形成数组
print("\nSplitting range [0, 10) with step 2:")
print(split_range_with_count(0, 10, 5))

# 生成指数间隔的数组
print("\nGenerating exponential array in [1, 100] with 5 points:")
print(generate_exponential_array(0, 2, 5))

# 生成网格数据点
x_range = np.linspace(0, 1, 3)
y_range = np.linspace(0, 1, 3)
print("\nGenerating grid points:")
print(generate_grid_points(x_range, y_range))
