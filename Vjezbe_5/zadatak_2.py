import numpy as np
import matplotlib.pyplot as plt

def funkcija(x):
    return np.sin(x)

def derivacija(f, x, dx=1e-6):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

x = np.linspace(-5, 5, 100)

y = derivacija(funkcija, x)

plt.plot(x, y, label='Derivacija funkcije sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

y_analiticko = np.cos(x)

plt.plot(x, y, label='Numeričko rješenje')
plt.plot(x, y_analiticko, label='Analitičko rješenje')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
