import ODE as ODE
import Matrix as Matrix
from gillespie import SSA
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

Susceptible = 995
Infected = 5
Imune = 0

X0 = (Susceptible, Infected, Imune)

N = Susceptible + Infected + Imune
gamma = 1/7
beta = 0.3
coeff= (N, gamma, beta)

t0 = 0
t_end = 120
tspan = (t0, t_end)

# times = np.arange(t0, t_end, 0.01)
sol = solve_ivp(ODE.ODE, tspan, X0, args=(coeff,), max_step = 1)

plt.figure(1)

for i in range(100):
    t,X = SSA(Matrix.prop, Matrix.stoch, X0, tspan, coeff)
    plt.plot(t,X[:,0],'y-')
    plt.plot(t,X[:,1],'r-')
    plt.plot(t,X[:,2],'g-')



plt.plot(t,X[:,0],'y-', label="Susceptible")
plt.plot(t,X[:,1],'r-', label="Infected")
plt.plot(t,X[:,2],'g-', label="Immune")
ax1 = plt.gca()
xmin, xmax, ymin, ymax = ax1.axis()
ax1.set(xlim=(0,xmax), ylim=(0, ymax))
plt.title("SIR-Model, stochastic")
plt.legend()

#plt.figure(2)
# plt.plot(sol.t,sol.y[0],"y-", label="Susceptible")
# plt.plot(sol.t,sol.y[1],"r-", label="Infected")
# plt.plot(sol.t,sol.y[2],"g-", label="Immune")

plt.plot(sol.t,sol.y[0],"k-", linewidth = 4)
plt.plot(sol.t,sol.y[1],"k-", linewidth = 4)
plt.plot(sol.t,sol.y[2],"k-", linewidth = 4)
ax2 = plt.gca()
# xmin, xmax, ymin, ymax = ax2.axis()
ax2.set(xlim=(0, xmax), ylim=(0, ymax))
plt.legend
plt.title("SIR-Model")
plt.show()
