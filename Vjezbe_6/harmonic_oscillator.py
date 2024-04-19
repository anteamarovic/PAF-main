import numpy as np
import matplotlib.pyplot as plt

class HarmonijskiOskilator:
    def __init__(self, x0, v0, k, m):
        self.x0 = x0
        self.v0 = v0
        self.k = k
        self.m = m

    def položaj(self, t):
        omega = np.sqrt(self.k / self.m)
        return self.x0 * np.cos(omega * t) + (self.v0 / omega) * np.sin(omega * t)

    def brzina(self, t):
        omega = np.sqrt(self.k / self.m)
        return -self.x0 * omega * np.sin(omega * t) + self.v0 * np.cos(omega * t)

    def ubrzanje(self, t):
        omega = np.sqrt(self.k / self.m)
        return -self.x0 * omega**2 * np.cos(omega * t) - self.v0 * omega * np.sin(omega * t)

# Testiranje klase HarmonijskiOskilator
ho = HarmonijskiOskilator(x0=1.0, v0=0.0, k=4.0, m=1.0)

# Vremenske vrijednosti
t = np.linspace(0, 10, 1000)

# Položaj u ovisnosti o vremenu
plt.figure()
plt.plot(t, ho.položaj(t))
plt.xlabel('Vrijeme (s)')
plt.ylabel('Položaj (m)')
plt.title('Položaj u ovisnosti o vremenu')
plt.show()

# Brzina u ovisnosti o vremenu
plt.figure()
plt.plot(t, ho.brzina(t))
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')
plt.title('Brzina u ovisnosti o vremenu')
plt.show()

# Ubrzanje u ovisnosti o vremenu
plt.figure()
plt.plot(t, ho.ubrzanje(t))
plt.xlabel('Vrijeme (s)')
plt.ylabel('Ubrzanje (m/s^2)')
plt.title('Ubrzanje u ovisnosti o vremenu')
plt.show()



