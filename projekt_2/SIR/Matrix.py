import numpy as np

def stoch():
    M=np.array([[-1, 1, 0],
                [0, -1, 1]])
    return M

# X[0] = S, X[1] = I, X[2] = R
def prop(X,coeff):
    N = coeff[0]
    gamma=coeff[1]
    beta=coeff[2]
    w=np.array([beta*(X[0]/N)*X[1], gamma*X[1]])
    return w