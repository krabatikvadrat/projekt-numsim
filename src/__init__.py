import numpy as np

arr = np.fromfile("Nbody/input_data/circles_N_4.gal", dtype=float)

print(arr)
print(len(arr))
N = int(len(arr)/6)
print(N)


