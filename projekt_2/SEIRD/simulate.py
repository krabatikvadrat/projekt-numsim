import ODE as ODE
import Matrix as Matrix
from gillespie import SSA
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

Susceptible = 995
Exposed = 0
Infected = 5
Imune = 0
Dead = 0

X0 = (Susceptible, Exposed, Infected, Imune, Dead)

N = Susceptible + Exposed + Infected + Imune + Dead
alpha = 1/4
gamma = 1/7
beta = 0.3
mu = 0.01
coeff= (N, gamma, beta, alpha, mu)

t0 = 0
t_end = 120
tspan = (t0, t_end)

# times = np.arange(t0, t_end, 0.01)
sol = solve_ivp(ODE.ODE, tspan, X0, args=(coeff,), max_step = 1)
t,X = SSA(Matrix.prop, Matrix.stoch, X0, tspan, coeff)

plt.figure(1)
plt.plot(t,X[:,0],'y-', label="Susceptible")
plt.plot(t,X[:,1],'m-', label="Exposed")
plt.plot(t,X[:,2],'r-', label="Infected")
plt.plot(t,X[:,3],'g-', label="Immune")
plt.plot(t,X[:,4],'c-', label="Dead")   
ax1 = plt.gca()
xmin, xmax, ymin, ymax = ax1.axis()
ax1.set(xlim=(0,xmax), ylim=(0, ymax))
plt.title("SEIRD-Model, stochastic")
plt.legend()

plt.figure(2)
plt.plot(sol.t,sol.y[0],"y-", label="Susceptible", linewidth=1)
plt.plot(sol.t,sol.y[1],"m-", label="Exposed", linewidth=1)
plt.plot(sol.t,sol.y[2],"r-", label="Infected", linewidth=1)
plt.plot(sol.t,sol.y[3],"g-", label="Immune", linewidth=1)
plt.plot(sol.t,sol.y[4],"c-", label="Dead", linewidth=1)
ax2 = plt.gca()
# xmin, xmax, ymin, ymax = ax2.axis()
ax2.set(xlim=(0, xmax), ylim=(0, ymax))
plt.legend
plt.title("SEIRD-Model, deterministic")
plt.show()
