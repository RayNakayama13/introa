import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import pickle


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28,28)
print(img.shape)

# img_show(img)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def soft_max(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    exp_sum = np.sum(np.exp(a - c))
    y = exp_a / exp_sum
    return y

def init_network():
    with open('deeplearning/ch03/sample_weight.pkl', 'rb') as f:
        network= pickle.load(f)
    return network

def get_data():
    (x_train, t_test), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = soft_max(a3)

    return y


x, t = get_data()
network = init_network()


accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

# print('Accuracy:' + str(float(accuracy_cnt)/ len(x)))


x, t = get_data()
network = init_network()

accuracy_cnt = 0
batch_size = 100

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p==t[i:i+batch_size])

print(accuracy_cnt)
print('Accuracy:' + str(float(accuracy_cnt) / len(x)))
