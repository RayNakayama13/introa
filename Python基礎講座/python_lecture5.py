# import numpy as np
# # from python_lecture6 import AND, NAND, OR
#
# class GATE():
#
#     def NAND(self, x1, x2):
#         x = np.array([x1, x2])
#         w = np.array([-0.5, -0.5])
#         b = 0.7
#         if np.sum(x * w) + b >= 0:
#             return 1
#         else:
#             return 0
#
#
#     def OR(self, x1, x2):
#         x = np.array([x1, x2])
#         w = np.array([0.5, 0.5])
#         b = -0.2
#         if np.sum(x * w) + b >= 0:
#             return 1
#         else:
#             return  0
#
#     def AND(self, x1, x2):
#         x = np.array([x1, x2])
#         w = np.array([0.5, 0.5])
#         b = -1.0
#         if np.sum(x * w) + b  >= 0:
#             return 1
#         else:
#             return 0
#
#     def XOR(self, x1, x2):
#         s1 = self.NAND(x1, x2)
#         s2 = self.OR(x1,  x2)
#         y = self.AND(s1, s2)
#         return y
#
# gate = GATE()
# print(gate.XOR(0,0))
# print(gate.XOR(1,0))
# print(gate.XOR(0,1))
# print(gate.XOR(1,1))



################################################################################################################################################################################################################################################







import numpy as np
import matplotlib.pylab as plt

# def step_func(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# x = np.array([1.0, -1.0, 2.0])
# y = x  > 0
# print(y)
# print(y.astype(np.int))


#0or1になるから階段のよう、　ステップ関数は階段関数と呼ばれる
# def step_func(x):
#     y = x > 0
#     return y.astype(np.int)
# x  = np.arange(-5.0, 5.0, 0.1)
# y = step_func(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# # plt.show()
#
# #step_funcとは違い滑らかな曲線を描く。
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
# z = sigmoid(x)
# plt.plot(x, z)
# plt.ylim(-0.1, 1.1)
# # plt.show()
#
# #ReLU(Rectified Linerar Unit)は入力が０を超えていれば入力値を出力し、０以下の場合には０を出力する。
# def relu(x):
#     return np.maximun(0, x)
#
#
# X = np.array([1.0, 0.5])
# W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
# B1 = np.array([0.1, 0.2, 0.3])
#
# A1 = np.dot(X, W1) + B1
# print(A1.shape)
# Z1 = sigmoid(A1)
# print(Z1.shape)
# #z1 = (0, 3)
#
# W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
# B2 = np.array([0.1, 0.2])
#
# A2 = np.dot(Z1, W2) + B2
# print(A2.shape)
# Z2 = sigmoid(A2)
#
# def identify_func(x):
#     return x
#
# W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
# B3 = np.array([0.1, 0.2])
#
# A3 = np.dot(Z2, W3) + B3
#
# Y = identify_func(A3)
# print(Y)
#
# def init_network():
#     network = {}
#     network['w1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
#     network['w2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
#     network['w3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
#     network['b1'] = np.array([0.1, 0.2, 0.3])
#     network['b2'] = np.array([0.1, 0.2])
#     network['b3'] = np.array([0.1, 0.2])
#     return network
#
# def forward(network, x):
#     W1, W2, W3 = network['w1'], network['w2'], network['w3']
#     B1, B2, B3 = network['b1'], network['b2'], network['b3']
#
#     a1 = np.dot(x, W1) + B1
#     z1 = sigmoid(a1)
#     a2 = np.dot(z1, W2) + B2
#     z2 = sigmoid(a2)
#     a3 = np.dot(z2, W3) + B3
#     y = identify_func(a3)
#
#     return y
#
# network = init_network()
# x = np.array([1.0, 0.5])
# y = forward(network, x)
# print(y)

################################################################################################################################################################


# a = np.array([0.3, 2.9, 4.0])
# exp_a = np.exp(a)
# print(exp_a)
#
# exp_sum = np.sum(np.exp(a))
# y = exp_a / exp_sum
# print(y)
#
#
# #cで引いたのはオーバーフローすることを避けるため。（オーバーフロー：数値が大きすぎて計算できなくなること）
# def soft_max(a):
#     c = np.max(a)
#     exp_a = np.exp(a - c)
#     exp_sum = np.sum(np.exp(a - c))
#     y = exp_a / exp_sum
#     return y


################################################################################################################################################################

import sys, os
sys.path.append(os.pardir)
import numpy as np
print(os.path.exists('Python Datetime'))
# from mnist import load_mnist
# from PIL import Image
