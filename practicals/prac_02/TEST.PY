import numpy as np
# 创建一个 4x3 的数据矩阵
X = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]])
# 创建一个 3x1 的权重矩阵
W = np.array([[0.1],
[0.2],
[0.3]])
# 矩阵乘法
Y = np.dot(X, W)
# 打印结果
print("Data Matrix (X):\n", X)
print("Weight Matrix (W):\n", W)
print("Result (Y = X * W):\n", Y)