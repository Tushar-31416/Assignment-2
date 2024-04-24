import numpy as np
import matplotlib.pyplot as plt



def rk4(fy,fz,x,y,z,h):
    k1 = h*fy(x,y,z)
    l1 = h*fz(x,y,z)
    k2 = h*fy(x+h/2,y+k1/2,z+l1/2)
    l2 = h*fz(x+h/2,y+k1/2,z+l1/2)
    k3 = h*fy(x+h/2,y+k2/2,z+l2/2)
    l3 = h*fz(x+h/2,y+k2/2,z+l2/2)
    k4 = h*fy(x+h,y+k3,z+l3)
    l4 = h*fz(x+h,y+k3,z+l3)
    return [y+(k1+2*k2+2*k3+k4)/6, z+(l1+l2*2+l3*2+l4)/6]



def fy(x,y,z):
    return (y + z)

def fz(x,y,z):
    return (z+x*np.exp(x)-x)




y = [0]
z = [0]
h = 0.01
x_min = 0
x_max = 1
N = int((x_max-x_min)/h)
x = [x_min]

for i in range(N):
    y.append(rk4(fy,fz,x_min+(i*h),y[i],z[i],h)[0])
    z.append(rk4(fy,fz,x_min+(i*h),y[i],z[i],h)[1])
    x.append(x_min+((i+1)*h))
#print('y = ',y)
print("z = ",z )

plt.plot(x,y)
#plt.plot(x,z,label='z')
plt.xlabel('x')
plt.ylabel('y')
#plt.legend()
plt.show()