import numpy as np
import matplotlib.pyplot as plt


#   QUESTION A ***************************************
x_min = 0
x_max = 1
h = 0.001
y_1=[np.e]
x_1 = [x_min]
N = int((x_max-x_min)*1.0/h)



def f1(x,y):
    return -9*y

def df1(x,y):
    return -9

tol=0.01
for i in range(N):
    t = 1
    y0 = 0
    while(t>tol):
        y1 = y0 - (h*f1(x_min+i*h,y0)+y_1[i]-y0)/(h*df1(x_min+i*h,y0)-1)  # SOLVING FOR THE ROOT BY NEWTON'S METHOD 
        t = np.abs(y1-y0)
        y0 = y1
    y_1.append(y0)
    x_1.append(x_min+(i+1)*h)





#   QUESTION B ***************************************

x_min = 0
x_max = 1
h = 0.001
y_2=[1.0/3]
x_2=[x_min]
N = int((x_max-x_min)*1.0/h)

def f2(x,y):
    return -20*(y-x)**2 + 2*x

def df2(x,y):
    return -40*(y-x)


tol = 0.01
for i in range(N):
    t = 1
    y0 = 0
    while(t>tol):
        y1 = y0 - (h*f2(x_min+i*h,y0)+y_2[i]-y0)/(h*df2(x_min+i*h,y0)-1)   # SOLVING FOR THE ROOT BY NEWTON'S METHOD 
        t = np.abs(y1-y0)
        y0 = y1
    y_2.append(y0)
    x_2.append(x_min+(i+1)*h)





plt.plot(x_1,y_1,label='y_1')
plt.plot(x_2,y_2,label='y_2')
plt.xlabel("x")
plt.legend()
plt.show()