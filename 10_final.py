import numpy as np
import matplotlib.pyplot as plt
from math import *


def rk4(f,t,y,h):
    k1 = h*f(t,y)
    k2 = h*f(t+h/2,y+k1/2)
    k3 = h*f(t+h/2,y+k2/2)
    k4 = h*f(t+h,y+k3)
    return y+(k1+2*k2+2*k3+k4)/6

def f(t,y):
    return (y**2+y)/t

t_min = 1
t_max = 3
h = 0.001
y=[-2]
t = [t_min]
a = 0 
while(a==0): #To make sure that the while condition is satisfied
    a = 1
    if (t[-1]+h<t_max):
        a  = a-1
        y1 = rk4(f,t[-1],y[-1],h)
        y.append(y1)
        t.append(t[-1]+h)
        y1 = rk4(f,t[-1],y[-1],h)
        y2 = rk4(f,t[-2],y[-2],2*h)
        rho = 1
        if (np.abs(y1-y2)!=0):
            rho = (10**(-4)*h*30/np.abs(y1-y2))**(0.25)
        h = h*rho


h = t_max - t[-1]
y.append(rk4(f,t[-1],y[-1],h)) #to reach the boundary point
t.append(t_max)


def truex(t):
    return -2*t/(-1+2*t)

error = np.linalg.norm(y-np.vectorize(truex)(t),ord=inf)
print('The final error truns out to be = ',error)



plt.plot(t,y,'red',label='Numerical')
for xc in t:
    plt.axvline(x=xc)

plt.plot(t,np.vectorize(truex)(t),'--',color='green',label='exact')


plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()