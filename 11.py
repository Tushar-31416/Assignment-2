import numpy as np
import matplotlib.pyplot as plt



def rk4(f,t,x,h):
    k1 = h*f(t,x)
    k2 = h*f(t+h/2,x+k1/2)
    k3 = h*f(t+h/2,x+k2/2)
    k4 = h*f(t+h,x+k3)
    return x+(k1+2*k2+2*k3+k4)/6

def f(t,x):
    return 1/(x**2+t**2)

t_min = 0
t_max = 3.5*10**6
h = 0.001
x = [1]
t = [t_min]
a = 0
 
while(a==0):
#for p in range(1):
    a = 1
    if (t[-1]+h<t_max):
        a  = a-1
        x1 = rk4(f,t[-1],x[-1],h)
#        print('y1_1 =',y1)
        x.append(x1)
        t.append(t[-1]+h)
        x1 = rk4(f,t[-1],x[-1],h)
#        print('y1_2 =',y1)
        x2 = rk4(f,t[-2],x[-2],2*h)
#        print('y2 =',y2)
        rho = 1
        if (np.abs(x1-x2)!=0):
            rho = (10**(-6)*h*30/np.abs(x1-x2))**(0.25)
        h = h*rho


#print('final time = ',t[-1])
h = t_max - t[-1]
xf = rk4(f,t[-1],x[-1],h)

print('The value of x at 3.5 * 10^(6) is: ',xf)

