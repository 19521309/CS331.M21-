import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.5)
n_sample = len(x)
noise = np.random.normal(0,1,n_sample)
y = 5*x - 6 +noise
plt.plot(x,y, 'ro')

theta0 = 10 
theta1= -4
alpha = 0.01
eps = 0.0001

while True:
      der_theta0 = np.mean(x*theta1 + theta0 - y)
      der_theta1 = np.mean((x*theta1 + theta0 - y)*x)
      theta0 = theta0 - alpha*der_theta0
      theta1 = theta0 - alpha*der_theta1
  
  #truc quan hoa ket qua, ve phuong trinh duong thang 
  #y = theta1*x + theta0
      x_vis = np.array([-5.0,5.0])
      y_vis = theta1*x_vis + theta0
      plt.plot(x_vis,y_vis)
      plt.pause(0.1)

      der_theta0 = np.mean(x*theta1 + theta0 - y)
      der_theta1 = np.mean((x*theta1 + theta0 - y)*x)
      if abs(der_theta0) < eps and abs(der_theta1)<eps:
       break
   
   
print('Gia tri toi uu cua theta0 = ', theta0)
print('Gia tri toi uu cua theta1 = ', theta1)

