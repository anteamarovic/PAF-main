import matplotlib.pyplot as plt
import numpy as np
import math

def funkcija(x):
    return (x**3)+(2*x**2)+x

def numericka_derivacija(f, x, h=0.01, metoda=3):
    if metoda == 2:
        df = ((f(x+h) - f(x)) / h)
    elif metoda == 3:
        df = ((f(x+h) - f(x)) / (2 * h))
    else:
        raise ValueError("Netočna vrijednost metode")
    return df

def derivacija_interval(f, a, b, h=0.01, metoda=2):
    tocke = np.arange(a, b + h, h)
    derivacije = []
    for t in tocke:
        derivacija = numericka_derivacija(f, t, h, metoda)
        derivacije.append(derivacija)
    return tocke, derivacije

def integral_pravokutna(f, a, b, N):
    dx = (b - a) / N
    tocke = np.linspace(a, b, N+1)
    sredine = (tocke[1:] + tocke[:-1]) / 2
    vrijednosti = f(sredine)
    donja_medja = np.sum(vrijednosti * dx)
    gornja_medja = np.sum(vrijednosti[::-1] * dx)
    return donja_medja, gornja_medja

def integral_trapezna(f, a, b, N):
    dx = (b - a) / N
    tocke = np.linspace(a, b, N+1)
    vrijednosti = f(tocke)
    donja_medja = 0
    gornja_medja = 0
    for i in range(N):
        donja_medja += (vrijednosti[i] + vrijednosti[i+1]) * dx / 2
        gornja_medja += (vrijednosti[N-i] + vrijednosti[N-i-1]) * dx / 2
    return donja_medja, gornja_medja

def trapezna_metoda(f, a, b, n):
    h = (b - a) / float(n)
    x = [a + i*h for i in range(n+1)]
    y = [f(x[i]) for i in range(n+1)]
    integral = (h/2) * (y[0] + y[n] + 2 * sum(y[1:n]))
    return integral

# Primjeri korištenja funkcija:

a = -5
b = 5
h = 0.1
metoda = 2
x, y = derivacija_interval(funkcija, a, b, h, metoda)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('derivacija')
ax.set_title('Numericka derivacija funkcije ')
plt.show() 

b = 0
a = 1
N = 100
donja_medja, gornja_medja = integral_pravokutna(funkcija, b, a, N)
print("Donja medja 1:", donja_medja)
print("Gornja medja 1:", gornja_medja)

a = 0
b = 1
N = 100
donja_medja, gornja_medja = integral_trapezna(funkcija, a, b, N)
print("Donja medja 2: ", donja_medja)
print("Gornja medja 2: ", gornja_medja)

integral = trapezna_metoda(funkcija, 0, 1, 10)
print("Numerička vrijednost integrala :", integral)
