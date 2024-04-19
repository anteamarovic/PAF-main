import numpy as np
import matplotlib.pyplot as plt

class HarmoničkiOskilator:

    def __init__(self, masa, opruga_konstanta, početni_položaj, početna_brzina, vremenski_korak):
        self.masa = masa
        self.opruga_konstanta = opruga_konstanta
        self.početni_položaj = početni_položaj
        self.početna_brzina = početna_brzina
        self.vremenski_korak = vremenski_korak

    def x(self, t):
        return self.početni_položaj * np.cos(np.sqrt(self.opruga_konstanta / self.masa) * t)

    def v(self, t):
        return -self.početni_položaj * np.sqrt(self.opruga_konstanta / self.masa) * np.sin(np.sqrt(self.opruga_konstanta / self.masa) * t)

    def a(self, t):
        return -self.početni_položaj * (self.opruga_konstanta / self.masa) * np.cos(np.sqrt(self.opruga_konstanta / self.masa) * t)

    def prikaži_grafove(self):
        vrijeme = np.arange(0, 10, self.vremenski_korak)
        x_vrijednosti = self.x(vrijeme)
        v_vrijednosti = self.v(vrijeme)
        a_vrijednosti = self.a(vrijeme)

        plt.figure(figsize=(14, 10))

        plt.subplot(3, 1, 1)
        plt.plot(vrijeme, x_vrijednosti)
        plt.title('Graf ovisnosti položaja o vremenu')

        plt.subplot(3, 1, 2)
        plt.plot(vrijeme, v_vrijednosti)
        plt.title('Graf ovisnosti brzine o vremenu')

        plt.subplot(3, 1, 3)
        plt.plot(vrijeme, a_vrijednosti)
        plt.title('Graf ovisnosti ubrzanja o vremenu')

        plt.tight_layout()
        plt.show()



