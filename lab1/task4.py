import math

def hypotenuse_length(side1, side2):
    """
    计算直角三角形的斜边长

    参数:
    side1: float，第一条直角边的长度
    side2: float，第二条直角边的长度

    返回值:
    float，直角三角形的斜边长
    """
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    return hypotenuse

# 测试函数
side1 = 3
side2 = 4
hypotenuse = hypotenuse_length(side1, side2)
print("直角三角形的斜边长为:", hypotenuse)

