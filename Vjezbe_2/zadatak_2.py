import numpy as np
import matplotlib.pyplot as plt

# Početni uvjeti
v0 = 100  # početna brzina u m/s
kut = 45  # kut otklona u stupnjevima

# Pretvaranje kuta u radiane
kut_radiani = np.radians(kut)

# Komponente ubrzanja
ay = -9.81  # vertikalna komponenta akceleracije (gravitacija)
ax = 0      # horizontalna komponenta akceleracije (brzina je konstantna)

# Početne brzine
vx = v0 * np.cos(kut_radiani)
vy = v0 * np.sin(kut_radiani)

# Inicijalizacija listi za pohranu podataka
lista_vx, lista_vy, lista_x, lista_y, lista_vremena = [], [], [], [], []

# Parametri simulacije
x, y, t, dt = 0, 0, 0, 0.01
simulacija_trajanje = 10

# Simulacija gibanja
while t <= simulacija_trajanje:
    lista_vremena.append(t)
    lista_vx.append(vx)
    lista_vy.append(vy)
    lista_x.append(x)
    lista_y.append(y)

    # Ažuriranje brzina i pozicija koristeći jednadžbe gibanja
    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x + vx * dt
    y = y + vy * dt

    t = t + dt

# Crtanje grafova
plt.subplot(1, 3, 1)
plt.plot(lista_x, lista_y)
plt.title('x-y Graf')
plt.xlabel('x (m)')
plt.ylabel('y (m)')

plt.subplot(1, 3, 2)
plt.plot(lista_vremena, lista_x)
plt.title('x-t Graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('x (m)')

plt.subplot(1, 3, 3)
plt.plot(lista_vremena, lista_y)
plt.title('y-t Graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('y (m)')

plt.tight_layout()
plt.show()