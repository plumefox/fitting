#一元线性回归
#拟合

import numpy as np
import matplotlib.pyplot as plt
#先输入x，y,
x=np.arange(150,270,10)
y=[56.9,58.3,61.6,64.6,68.1,71.3,74.1,77.4,80.2,82.6,86.4,89.7]

def get_average(list):#获取平均数
    return sum(list)/len(list)
def Sum_of_Squares(list):
    Sum=0
    for i in range(len(list)):#平方和
        X=list[i]**2
        Sum += X
    return Sum
def lxx(list):
    Sum=Sum_of_Squares(list)
    return Sum-sum(list)**2/len(list)
def multiplication(list1,list2):
    Sum=0
    for i in range(len(list1)):
        Sum+=list1[i]*list2[i]
    return Sum
def lxy(list1,list2):
    mul=multiplication(list1,list2)
    Sum_x_y=sum(list1)*sum(list2)
    return mul-Sum_x_y/len(list1)


b=lxy(x,y)/lxx(x)
a=get_average(y)-b*get_average(x)
print(b)
print(a)
print("y="+str(a)+"+"+str(b)+"x")

plt.axis([130, 270, 50, 100])
plt.plot(x,y,'o',x,a+b*x,'r')
plt.show()