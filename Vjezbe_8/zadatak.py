import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #uvodimo datoteku za 3d crtanje 

class Čestica: #definiramo klasu cestica za elektromagnetso polje
    def __init__(self, masa, q, E, B, v0, x0, dt=0.01):
        self.masa = masa
        self.q = q
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)
        self.x0 = np.array(x0, dtype=float)
        self.dt = dt
        self.reset()

    def reset(self): #definiramo metodu koja resetira polzaj cestica i prazne liste
        self.x = []
        self.y = []
        self.z = []
        self.v = self.v0
        self.x.append(self.x0[0])
        self.y.append(self.x0[1])
        self.z.append(self.x0[2])

    def putanja(self, T):
        t_vrijednosti = np.arange(0.0, T + self.dt, self.dt) #postavlja ka granice od nula do t sa korakom dt
        broj_koraka = len(t_vrijednosti)

        for i in range(1, broj_koraka):
            ubrzanje = (self.q / self.masa) * (self.E + np.cross(self.v, self.B)) #koristimo lorenzovu silu 
            self.v += ubrzanje * self.dt  #azurira brzinu cestice
            self.x0 += self.v * self.dt  #azurira polozaj cestice
            self.x.append(self.x0[0])  #dodavanje novih kordinata 
            self.y.append(self.x0[1])
            self.z.append(self.x0[2])

        return self.x, self.y, self.z

E = (0, 0, 0)
B = (0, 0, 1)
v = (0.1, 0.1, 0.1)
x = (0, 0, 0)

p1 = Čestica(1, 1, E, B, v, x) #stvaramo konkretnu cesticu pomocu vec definirane čestice iz klase 
p2 = Čestica(1, -1, E, B, v, x)

x1, y1, z1 = p1.putanja(50) #putanja pozitrona za t=50
x2, y2, z2 = p2.putanja(50) #putanja elektrona za t=50

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1, c="r", label="pozitron")
ax.plot3D(x2, y2, z2, c="b", label="elektron")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("z [m]")
ax.set_title("Usporedba gibanja elektrona i pozitrona u konstantnom magnetskom polju")
ax.legend()
plt.show()

p1.reset()
p2.reset()

