import numpy as np

def stoch():
    M=np.array([[-1, 1, 0, 0, 0, 0],
               [0, -1, 1, 0, 0, 0],
               [0, 0, -1, 1, 0, 0],
               [0, 0, -1, 0, 1, 0],
               [-1, 0, 0, 0, 0, 1]])
    return M

# X[0] = S, X[1] = E, X[2] = I, X[3] = R, X[4] = D, X[5] = V
def prop(X,coeff):
    N = coeff[0]
    gamma=coeff[1]
    beta=coeff[2]
    alpha = coeff[3]
    mu = coeff[4]
    nu = coeff[5]

    w=np.array([beta*(X[2]/N)*X[0], alpha*X[1], gamma*X[2], mu*X[2], nu])
    return w