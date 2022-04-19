#cài đặt thư viện cần thiết
import numpy as np
#thư viện để vẽ biểu đồ
import matplotlib.pyplot as plt

#phát sinh dữ liệu
#Tạo dữ liệu X có giá trị từ -5 đến 5 
#với bước nhảy bằng 0.5
x = np.arange(-5,5,0.5)
#Giá trị n_sample là số lượng phần tử (dữ liệu) của mảng X
n_sample = len(x)
#Giá trị noise - nhiễu thống kê 
#liên quan đến sự biến thiên trong mẫu
#Nhiễu được biển diễn dưới dạng biến ngẫu nhiên
noise = np.random.normal(0,1,n_sample)
#Khởi tạo giá trị Y
Y = 5*x - 6 +noise
#biểu diễn x và Y trên đồ thị dưới dạng chấm tròn màu đỏ
plt.plot(x,Y, 'ro')


# Tạo một mảng gồm những giá trị 1
# mảng có độ dài bằng độ dài của mảng x
ones = np.ones((1,n_sample))
# Mảng X là mảng được gộp bởi mảng những giá trị 1 
# và mảng x đã được khởi tạo ở trên
X = np.concatenate((ones, [x]))
#In mảng X
print(X)
#In mảng Y
print(Y)
#khởi tạo giá trị theta, alpha,eps
theta = np.array([[10],[-5]])
alpha = 0.01
eps = 0.0001


#Lặp
#Cập nhật tham số
#Kiểm tra điểm dừng của vòng lặp
while True:
    #Tích của X và theta chuyển vị trừ cho Y 
    #Lấy chuyển vị của hiệu số nhân với X 
    #Tất cả chia n_sample
    #Đạo hàm theo vector theta
    nabla = (1.0/n_sample)*np.dot(X, (np.dot(theta.T, X) - Y).T)
    #Cập nhật theta để thay đổi nabla ở bước sau  
    theta = theta - alpha*nabla
    
    #Trực quan hóa kết quả, vẽ phương trình đường thẳng 
    #y = theta1*x + theta0
    
    #trực quan hóa dữ liệu
    x_vis = np.array([-5.0,5.0])
    y_vis = theta[1][0]*x_vis + theta[0][0]
    plt.plot(x_vis,y_vis)
    plt.pause(0.1)
    
    #Tính lại nabla
    nabla = (1.0/n_sample)*np.dot(X, (np.dot(theta.T, X) - Y).T)
    if abs(nabla[0][0]) < eps and abs(nabla[1][0]) < eps:
        break
   
#In kết quả   
print('Gia tri toi uu cua theta = ', theta)
plt.show()

