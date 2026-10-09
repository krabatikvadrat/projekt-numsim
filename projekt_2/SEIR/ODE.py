import numpy as np

# X[0] = S, X[1] = E, X[2] = I, X[3] = R

def ODE(t, X, coeff):
    N = coeff[0]
    gamma = coeff[1]
    beta = coeff[2]
    alpha = coeff[3]
    
    y_prim = np.zeros(4)

    snopp = beta * X[0] * (X[2] / N)
    kuk = alpha * X[1]
    penis = gamma * X[2]

    y_prim[0] = -snopp
    y_prim[1] = snopp - kuk
    y_prim[2] = kuk - penis
    y_prim[3] = penis

    return y_prim
