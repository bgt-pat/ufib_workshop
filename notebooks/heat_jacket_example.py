import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp


def step_func()



def f(t,y,params):

    k1, Qm, k2, F, T0j = params

    yd = np.empty_like(y)

    eps = (273.15 + 20) - y[0]
    Kp = 0.8*eps
    Ki = 0.001*y[2]

    yd[0] = k1*(y[1] - y[0])
    yd[1] = k2*(y[0] - y[1]) + F*(T0j - y[1])
    yd[2] = eps

    Kd = 0.0*yd[0]
    yd[0] += Qm*(Kp + Kd + Ki)

    return yd

def main():


    phi = 0.01 # mass flow rate
    phi = 800./3600.


    uv = 0.1 # valve openness

    cp = 4200.
    cpj = 3500.

    M = 100.
    m = 20.

    U = 400.
    A = 0.3

    k1 = U*A/(M*cp)
    k2 = U*A/(m*cpj)

    Qm = +300./(M*cp)

    F = uv*phi*cpj/(m*cpj)

    tmax = 1000
    t = (0,tmax*60)
    t_eval = np.linspace(t[0],t[1],1001)

    y0 = [273.15 + 80., 273.15 - 10., 0.0]
    T0j = 273.15 - 10.

    sol = solve_ivp(fun=lambda t, y: f(t,y,(k1, Qm, k2, F, T0j)),t_span=t,y0=y0,t_eval=t_eval,method='Radau',
        rtol = 1e-4,
        atol = 1e-7)

    print("Vessel Temperature at Steady State = {}".format(T0j + Qm*M*cp/(uv*phi*cpj) + Qm*M*cp/(U*A)))
    print(sol.y[0,-1])

    print("Jacket Temperature at Steady State = {}".format(T0j + Qm*M*cp/(uv*phi*cpj)))
    print(sol.y[1,-1])

    tmin = t_eval/60

    plt.figure()
    plt.plot(tmin,sol.y[0,:] - 273.15,label="Temperature")
    plt.plot(tmin,sol.y[1,:] - 273.15,label="Jacket")

    plt.legend(loc=0)
    plt.xlabel("Time (min)")
    plt.ylabel("Temperature (°C)")


    plt.figure()
    plt.plot(tmin,sol.y[0,:] - 273.15 - 20,label="eps")

    plt.show()

if __name__ == '__main__':
    main()

