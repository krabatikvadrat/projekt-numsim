import numpy as np

# y[0] = S, y[1] = I, y[2] = R

def ODE(t, y, coeff):
    N = coeff[0]
    gamma=coeff[1]
    beta=coeff[2]
    
    y_prim = np.zeros(3)

    foo = beta * y[0] * (y[1] / N)
    bar = gamma * y[1]

    y_prim[0] = -foo
    y_prim[1] = foo - bar
    y_prim[2] = bar

    return y_prim
