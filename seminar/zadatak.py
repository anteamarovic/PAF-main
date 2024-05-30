import matplotlib.pyplot as plt
import numpy as np
import math

def provjeri_poziciju_tocke(tocka, ishodiste, radijus, spremi_sliku=False, ime_slike=None):
    # Računanje udaljenosti
    udaljenost = np.linalg.norm(np.array(tocka) - np.array(ishodiste))
    
    # Provjera položaja točke
    if udaljenost < radijus:
        pozicija = "unutar"
    elif udaljenost == radijus:
        pozicija = "na"
    else:
        pozicija = "izvan"
    
    # Crtanje kruznice i točke
    fig, ax = plt.subplots()
    krug = plt.Circle(ishodiste, radijus, edgecolor='blue', facecolor='none')
    ax.add_patch(krug)
    ax.plot(tocka[0], tocka[1], 'ro', label='Točka')
    ax.set_aspect('equal', adjustable='datalim')
    ax.legend()
    
    # Ispis rezultata
    print(f"Točka je {pozicija} kruznice i udaljenost je: {abs(udaljenost - radijus):.2f}")
    
    # Prikazivanje ili spremanje slike
    if spremi_sliku:
        if ime_slike:
            plt.savefig(f"{ime_slike}.png")
        else:
            plt.savefig("pozicija_tocke_kruznice.png")
    else:
        plt.show()

# Primjeri korištenja
provjeri_poziciju_tocke([2, 3], [0, 0], 5, spremi_sliku=True, ime_slike="slika_kruznice")
provjeri_poziciju_tocke([6, 8], [0, 0], 5)
provjeri_poziciju_tocke([3, 4], [0, 0], 5, spremi_sliku=True, ime_slike="kruznica2")
provjeri_poziciju_tocke([-2, -3], [0, 0], 5)