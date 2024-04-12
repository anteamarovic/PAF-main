import matplotlib.pyplot as plt
import numpy as np

def funkcija(x):
    return (x**3)+(2*x**2)+x

def numericka_derivacija(f, x, h=0.01):
    df = ((f(x+h) - f(x)) / h)
    return df

def derivacija_intervala(f, a, b, h=0.01):
    točke = np.arange(a, b + h, h)
    derivacije = [numericka_derivacija(f, t, h) for t in točke]
    return točke, derivacije

def integral_pravokutnika(f, a, b, N):
    dx = (b - a) / N
    točke = np.linspace(a, b, N+1)
    sredine = (točke[1:] + točke[:-1]) / 2
    vrijednosti = f(sredine)
    return np.sum(vrijednosti * dx)

def integral_trapeza(f, a, b, N):
    dx = (b - a) / N
    točke = np.linspace(a, b, N+1)
    vrijednosti = f(točke)
    return (dx/2) * (vrijednosti[0] + vrijednosti[N] + 2 * sum(vrijednosti[1:N]))

# Primjer korištenja funkcija:

a = -5
b = 5
h = 0.1
x, y = derivacija_intervala(funkcija, a, b, h)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('derivacija')
ax.set_title('Numerička derivacija funkcije ')
plt.show()

b = 0
a = 1
N = 100
integral_pravokutnik = integral_pravokutnika(funkcija, b, a, N)
print("Integral pravokutnika: ", integral_pravokutnik)

a = 0
b = 1
N = 100
integral_trapez = integral_trapeza(funkcija, a, b, N)
print("Integral trapeza: ", integral_trapez)

