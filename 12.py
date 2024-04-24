import numpy as np
import matplotlib.pyplot as plt



def rk4(f1,f2,f3,t,u1,u2,u3,h):
    k1 = [h*f1(t,u1,u2,u3),h*f3(t,u1,u2,u3),h*f3(t,u1,u2,u3)]
    k2 = [h*f1(t+h/2,u1+k1[0]/2,u2+k1[1]/2,u3+k1[2]/2),h*f2(t+h/2,u1+k1[0]/2,u2+k1[1]/2,u3+k1[2]/2),h*f3(t+h/2,u1+k1[0]/2,u2+k1[1]/2,u3+k1[2]/2)]
    k3 = [h*f1(t+h/2,u1+k2[0]/2,u2+k2[1]/2,u3+k2[2]/2),h*f2(t+h/2,u1+k2[0]/2,u2+k2[1]/2,u3+k2[2]/2),h*f3(t+h/2,u1+k2[0]/2,u2+k2[1]/2,u3+k2[2]/2)]
    k4 = [h*f1(t+h,u1+k3[0],u2+k3[1],u3+k3[2]),h*f2(t+h,u1+k3[0],u2+k3[1],u3+k3[2]),h*f3(t+h,u1+k3[0],u2+k3[1],u3+k3[2])]
    return [u1 + (k1[0]+2*k2[0]+2*k3[0]+k4[0])/6, u2 + (k1[1]+2*k2[1]+2*k3[1]+k4[1])/6, u3 + (k1[2]+2*k2[2]+2*k3[2]+k4[2])/6]

def f1(t,u1,u2,u3):
    return u1+2*u2-2*u3+(np.e)**(-t)

def f2(t,u1,u2,u3):
    return u2+u3-2*(np.e)**(-t)

def f3(t,u1,u2,u3):
    return u1+2*u2+(np.e)**(-t)


t_min = 0
t_max = 1
h = 0.01
N=int((t_max-t_min)/h)


u1 = [3]
u2 = [-1]
u3 = [1]
t = [0]

for i in range(N):
    u1.append(rk4(f1,f2,f3,t[i],u1[i],u2[i],u3[i],h)[0])
    u2.append(rk4(f1,f2,f3,t[i],u1[i],u2[i],u3[i],h)[1])
    u3.append(rk4(f1,f2,f3,t[i],u1[i],u2[i],u3[i],h)[2])
    t.append(t_min+(i+1)*h)

plt.plot(t,u1,label='u1')
plt.plot(t,u2,label='u2')
plt.plot(t,u3,label='u3')
plt.legend()
plt.show()


