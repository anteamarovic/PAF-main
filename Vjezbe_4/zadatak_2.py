import particle as pt
import numpy as np
import matplotlib.pyplot as plt
import math

adomet = []
ndomet = []
error = []

def analiticki_domet(v0, kut, x0, y0):
    kut_radiani = kut * (math.pi / 180)
    ay = -9.81 
    vx = v0 * math.cos(kut_radiani) 
    vy = v0 * math.sin(kut_radiani)
    t = -2 * vy / ay
    return x0 + vx * t

ad = analiticki_domet(10, 60, 0, 0)

# Izračun analitičkog dometa
for _ in np.arange(0.0001, 0.1, 0.0001):
    adomet.append(ad)

# Izračun numeričkog dometa i greške
for t in np.arange(0.0001, 0.1, 0.0001):
    p = pt.Particle(10, 60, 0, 0)
    nd = p.domet(t)
    ndomet.append(nd)

    error.append(100 * abs(ad - nd) / ad)

# Plotanje grafa
plt.plot(np.arange(0.0001, 0.1, 0.0001), error)
plt.xlabel("t [s]")
plt.ylabel("Apsolutna relativna pogreška [%]")
plt.title("Apsolutna relativna pogreška za domet projektila")
plt.show()
