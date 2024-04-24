import numpy as np
import matplotlib.pyplot as plt



def Euler(fy,fv,t,y,v,h):
    return [y+h*fy(t,y,v),v+h*fv(t,y,v)]
def fy(t,y,v):
    return v
def fv(t,y,v):
    return 2*v/t - 2*y/(t**2) + t*np.log(t)



t_min = 1
t_max = 2
h = 0.001
N = int((t_max-t_min)/h)

t=[t_min]
y=[1]
v=[0]



for i in range(N):
    y.append(Euler(fy,fv,t[i],y[i],v[i],h)[0])
    v.append(Euler(fy,fv,t[i],y[i],v[i],h)[1])
    t.append(t_min+((i+1)*h))


def real(t):
    s = []
    for l in range(len(t)):
        s.append(7*t[l]/4 + t[l]**3*np.log(t[l])/2 - 3*t[l]**3/4)
    return s




plt.plot(t,y,color='red',label='Euler')
plt.plot(t,real(t),'--',label='actual')
plt.xlabel('t')
plt.ylabel('y')

plt.legend()
plt.show()

