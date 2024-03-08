import matplotlib.pyplot as plt
import numpy as np

def gibanje(F, m, trajanje=10, korak_vremena=0.01):
    a = F / m
    x, v, t = [0], [0], [0]

    for _ in range(int(trajanje / korak_vremena)):
        a_trenutno = a
        v_trenutno = v[-1] + a_trenutno * korak_vremena
        x_trenutno = x[-1] + v_trenutno * korak_vremena

        t.append(t[-1] + korak_vremena)
        v.append(v_trenutno)
        x.append(x_trenutno)

    # Crtanje grafova
    plt.plot(t, x, label='x - t Graf')
    plt.xlabel('Vrijeme [s]')
    plt.ylabel('Položaj [m]')
    plt.legend()
    plt.show()

    plt.plot(t, v, label='v - t Graf')
    plt.xlabel('Vrijeme [s]')
    plt.ylabel('Brzina [m/s]')
    plt.legend()
    plt.show()

    plt.plot(t, [a] * len(t), label='a - t Graf')
    plt.xlabel('Vrijeme [s]')
    plt.ylabel('Ubrzanje [m/s^2]')
    plt.legend()
    plt.show()

# Pozivanje funkcije za jednoliko gibanje
gibanje(33, 63)
