import numpy as np

def f(t,y):
    return ((y*1.0/t)-(y*1.0/t)**2)

y = [1] #INITIAL VALUE
t_min=1
t_max=2
h = 0.1
N = int((t_max-t_min)/h)
for i in range(N):
    y.append(y[i]+h*f(t_min+(i*h),y[i]))
print(y)

def actual(t):
    return (t*1.0/(1+np.log(t)))

abs_error = np.abs(y[-1]-actual(t_max))
print("The absolute error is ",abs_error)

rel_error = abs_error/actual(t_max)
print("The relative error is ",rel_error)