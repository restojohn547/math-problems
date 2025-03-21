import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * x - 2

x_values = np.linspace(-3, 3, 100)
y_values = f(x_values)

plt.plot(x_values, y_values, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function f(x) vs. x values')
plt.legend()
plt.grid(True)
plt.show()

def g(x):
    return (5 - 1 / x)**2

y_values = g(x_values)

plt.plot(x_values, y_values, label='g(x)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Function g(x) vs. x values')
plt.legend()
plt.grid(True)
plt.show()
