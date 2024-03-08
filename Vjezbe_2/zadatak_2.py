import numpy as np
import matplotlib.pyplot as plt
import math

v0 = 33
kut = 53
kut_radiani = kut * (math.pi / 180)
ay = -9.81
ax = 0
vx = v0 * math.cos(kut_radiani)
vy = v0 * math.sin(kut_radiani)
lista_vx = []
lista_vy = []
lista_x = []
lista_y = []
lista_vremena = []
x = 0
y = 0
t = 0
dt = 0.01

while t <= 10:
    lista_vremena.append(t)
    vx = vx + ax * dt
    lista_vx.append(vx)
    vy = vy + ay * dt
    lista_vy.append(vy)
    x = x + vx * dt
    lista_x.append(x)
    y = y + vy * dt
    lista_y.append(y)
    t = t + dt

plt.subplot(1, 3, 1)
plt.plot(lista_x, lista_y)
plt.title("x-y graf")
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.subplot(1, 3, 2)
plt.plot(lista_vremena, lista_x)
plt.title("x-t graf")
plt.xlabel("Vrijeme [s]")
plt.ylabel("x [m]")

plt.subplot(1, 3, 3)
plt.plot(lista_vremena, lista_y)
plt.title("y-t graf")
plt.xlabel("Vrijeme [s]")
plt.ylabel("y [m]")

plt.show()
