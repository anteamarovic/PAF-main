import numpy as np
import matplotlib.pyplot as plt

G = 6.67408e-11  #gravitacijska konstanta [Nm^2/kg^2]
MS = 1.989e30  #masa sunca [kg]
MZ = 5.9742e24  #masa zemlje [kg]
AU = 1.486e11  #astronomska jedinica [m]
v_perpendicular = 29783  #okomita komponenta brzine zemlje [m/s]
korak_vremena = 24 * 60 * 60  #dan u sekundama

class Sustav:
    def __init__(self, masa1, masa2, polozaj1, polozaj2, brzina1, brzina2, dt):
        self.masa1 = masa1
        self.masa2 = masa2
        self.polozaj1 = np.array(polozaj1, dtype=float) #naredba array za stvranaje nizova 
        self.polozaj2 = np.array(polozaj2, dtype=float)
        self.brzina1 = np.array(brzina1, dtype=float)
        self.brzina2 = np.array(brzina2, dtype=float)
        self.dt = dt
        self.G = G
        self.putanje1 = []
        self.putanje2 = []

    def simuliraj(self, trajanje_dana):
        trajanje = trajanje_dana * self.dt
        for _ in range(int(trajanje / self.dt)):
            r = self.polozaj2 - self.polozaj1
            udaljenost = np.linalg.norm(r) #euklidska udaljenost dva tijela
            a1 = (self.G * self.masa2 / udaljenost**3) * r #akcleleracija zemlje uzrokovana suncem 
            self.brzina1 += a1 * self.dt #azuriranje brzina
            self.polozaj1 += self.brzina1 * self.dt
            self.putanje1.append(self.polozaj1.copy())
            a2 = -(self.G * self.masa1 / udaljenost**3) * r
            self.brzina2 += a2 * self.dt
            self.polozaj2 += self.brzina2 * self.dt
            self.putanje2.append(self.polozaj2.copy())
        return np.array(self.putanje1), np.array(self.putanje2)

# Pokretanje simulacije
sustav = Sustav(MZ, MS, [AU, 0], [0, 0], [0, v_perpendicular], [0, 0], korak_vremena)
putanja_zemlje, putanja_sunca = sustav.simuliraj(365.242)

# Crtanje putanja
plt.figure(figsize=(10, 10))
plt.plot(putanja_sunca[:, 0], putanja_sunca[:, 1], 'yo', label='Sunce')
plt.plot(putanja_zemlje[:, 0], putanja_zemlje[:, 1], 'b.', label='Zemlja')
plt.scatter(0, 0, color='yellow', marker='o', label='Ishodište (Sunce)')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Putanja Sunca i Zemlje')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()


