# Assignment-2

Question 3:
Here the given second order differential equation is divided into two coupled differential equations of variable 'y' and 'z', where 


```math
z' = z + x e^{x} - x 
```
```math
y' = y + z
```

Question 6:
The "numpy.argmin" can be used to find the cruve with minimum deviation of the final point from the given boundary condition while generating curves with a range of initial first derivative value. However, this method works only if the actual first derivative is contained in the range the intial derivatives were considered. Which again seem like a very time consuming process as the range has to large enough and further the convergence towards the actual value is much slower than 'secent method', which I have considered in the code.



15. 3 GSL functions for solving the initial value problems are:

1.gsl odeiv2 step rkf45

API: int gsl odeiv2 step rkf45 (const gsl odeiv2 step type * T, double t, const double y[ ], double h,
double yerr[ ], double ynew[ ], gsl odeiv2 system * sys)

Algorithm: Runge-Kutta-Fehlberg (RKF45)

2.gsl odeiv2 step rk4

API: int gsl odeiv2 step rk4 (const gsl odeiv2 step type * T, double t, const double y[ ], double h, double
y new[ ], gsl odeiv2 system * sys)

Algorithm: Classical Fourth-order Runge-Kutta

3.gsl odeiv2 step bsimp

API: int gsl odeiv2 step bsimp (const gsl odeiv2 step type * T, double t, const double y[ ], double h,
double * y new, double * yerr, gsl odeiv2 system * sys)

Algorithm: Bulirsch-Stoer Extrapolation

