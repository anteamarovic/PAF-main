import matplotlib.pyplot as plt
import numpy as np
import math

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

gibanje(33, 63)

def kosi_hitac(v0,kut,T): 
    kut_radiani=kut*(math.pi/180)
    ay=-9.81  
    ax=0     
    vx= v0 *math.cos(kut_radiani) 
    vy= v0 *math.sin(kut_radiani)
    lista_vx=[]
    lista_vy=[]
    lista_x=[]
    lista_y=[]
    lista_vremena=[]
    x=0
    y=0 
    t=0
    dt=0.01
    while t<=T:
        lista_vremena.append(t)
        vx=vx+ax*dt
        lista_vx.append(vx)
        vy=vy+ay*dt
        lista_vy.append(vy)
        x=x + vx*dt
        lista_x.append(x)
        y=y + vy*dt
        lista_y.append(y)
        t=t+dt
    plt.subplot(1,3,1)
    plt.plot(lista_x, lista_y)
    plt.subplot(1,3,2)
    plt.plot(lista_vremena, lista_x)
    plt.subplot(1,3,3)
    plt.plot(lista_vremena, lista_y)
    plt.show()