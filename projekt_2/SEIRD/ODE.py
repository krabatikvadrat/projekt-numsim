import numpy as np

# X[0] = S, X[1] = E, X[2] = I, X[3] = R, X[4] = D

def ODE(t, X, coeff):
    N = coeff[0]
    gamma = coeff[1]
    beta = coeff[2]
    alpha = coeff[3]
    mu = coeff[4]
    
    y_prim = np.zeros(5)

    snopp = beta * X[0] * (X[2] / N)
    kuk = alpha * X[1]
    penis = gamma * X[2]
    dase = mu * X[2]

    y_prim[0] = -snopp
    y_prim[1] = snopp - kuk
    y_prim[2] = kuk - penis - dase
    y_prim[3] = penis
    y_prim[4] = dase

    return y_prim
