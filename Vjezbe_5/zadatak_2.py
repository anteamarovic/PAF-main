import numpy as np
import matplotlib.pyplot as plt

# Definiraj funkciju
def funkcija(x):
    return np.sin(x)

# Definiraj funkciju za derivaciju
def derivacija(f, x, dx=1e-6):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

# Definiraj vrijednosti x
x = np.linspace(-5, 5, 1000)

# Izračunaj derivaciju
y = derivacija(funkcija, x)

# Prikaži derivaciju
plt.plot(x, y, label='Derivacija funkcije sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Analitičko rješenje
y_analiticko = np.cos(x)

# Prikaži numeričko i analitičko rješenje
plt.plot(x, y, label='Numeričko rješenje')
plt.plot(x, y_analiticko, label='Analitičko rješenje')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
