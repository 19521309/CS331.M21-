#Import các thư viện cần thiết
import numpy as np
import tensorflow as tf

# Mô hình Linear Regression
class LinearModel(object):
    def __init__(self):
        self.theta1 = tf.Variable(10.0)
        self.theta0 = tf.Variable(-3)

    def __call__(self, inputs):
        return self.theta1 * inputs + self.theta0

#Loss Function
def compute_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true-y_pred))

# Khởi tạo các giá trị
model = LinearModel()
theta1 = 0.01
theta0 = 0.0001

data = 100
inputs  = tf.random.normal(shape=[data])
noise   = tf.random.normal(shape=[data])
outputs = inputs * theta1 + theta0 + noise

# In kết quả
print(inputs)
print(noise)
print(outputs)



