#include <stdio.h>
#include <math.h>


double exact_sol(double t) {
    return pow(t + 1, 2) - 0.5 * exp(t);
}

double fun(double t, double y) {
    return y - pow(t, 2) + 1;
}

double euler_method(double t_min, double y0, double h, double t_max) {
    double t = t_min;
    double y = y0;
    while (t < t_max) {
        double error_bound = 0.5 * h *  (0.5*exp(2)-2)* (exp(t)-1); // Error bound derived in class
        double exact = exact_sol(t);
        double error = fabs(exact - y);
        printf("t = %.2f, y = %.6f, exact = %.6f, error = %.6f, error bound = %.6f\n", t, y, exact, error, error_bound);
        y = y + h * fun(t, y);
        t = t + h;
    }
    return y;
}

int main() {
    double t_min = 0.0;
    double y0 = 0.5;
    double h = 0.2;
    double t_max = 2.0;
    printf("The Euler's method with h = %.1f\n", h);
    euler_method(t_min, y0, h, t_max);
    return 0;
}