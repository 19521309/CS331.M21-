
#import các thư viện cần thiết
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

# chiều cao(cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# cân nặng (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
# Hiện thị dữ liệu 
plt.plot(X, y, 'ro')
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Tính tóan cân nặng 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
theta = np.dot(np.linalg.pinv(A), b)
print('theta = ', theta)

# Khởi tạo theta
theta0 = theta[0][0]
theta1 = theta[1][0]
x0 = np.linspace(145, 185, 2)
# Hàm h(x)
y0 = theta1*x0 + theta0

# Hiển thị
plt.plot(X.T, y.T, 'ro')      
plt.plot(x0, y0)              
plt.axis([140, 190, 45, 75])
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.show()

theta =  [[-33.73541021][0]]

y1 = theta1*155 + theta0
y2 = theta1*178 + theta0

print( u'Du doan can nang cua 1 nguoi cao 155 cm: %.2f (kg)'  %(y1) )
print( u'Du doan can nang cua 1 nguoi cao 178 cm: %.2f (kg)'  %(y2) )