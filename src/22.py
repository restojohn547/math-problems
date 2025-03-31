import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dS_dt(t, S):
    return -0.1 * S + 3 * (1 - S) / 4

def u(x, t): 
    y = odeint(dS_dt, x[0], t, full_output=True)
    S = y[:, -1]
    return S

t = np.linspace(0, 20, 1000)

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, u([0.5, 0.7], t), label="dS_dt= -0.1 * S + 3 * (1 - S) / 4")
plt.xlabel("t (seconds)")
plt.ylabel("S(t) (kg)")
plt.title("Solution of dS/dt = -0.1 * S + 3 * (1 - S) / 4 ")
plt.legend()
plt.show()
