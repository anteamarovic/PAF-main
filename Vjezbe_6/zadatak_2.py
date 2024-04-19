class HarmoničkiOskilator:
    # ...

    def numeričko_razdoblje(self, delta_t):
        # Numerički izračunajte i vratite period oscilacije
        # Inicijalizirajte vrijeme i položaj
        t = 0
        x = self.početni_položaj

        # Inicijalizirajte prethodnu i trenutnu brzinu
        preth_v = self.početna_brzina
        tren_v = self.v(delta_t)

        # Pronađite vrijeme kada oscilator prvi put prolazi kroz položaj ravnoteže
        while np.sign(preth_v) == np.sign(tren_v):
            t += delta_t
            x = self.x(t)
            preth_v = tren_v
            tren_v = self.v(t + delta_t)

        # Vrijeme kada oscilator prvi put prolazi kroz položaj ravnoteže je polovica perioda
        return 2 * t

# ...

# Testirajte preciznost metode numeričko_razdoblje za različite korake ∆t
delta_ts = [0.1, 0.01, 0.001, 0.0001]
for delta_t in delta_ts:
    # Stvorite instancu klase HarmoničkiOskilator
    oscilator = HarmoničkiOskilator(masa, opruga_konstanta, početni_položaj, početna_brzina, delta_t)

    # Izračunajte period koristeći analitičku i numeričku metodu
    period_analitički = oscilator.period()
    period_numerički = oscilator.numeričko_razdoblje(delta_t)

    # Izračunajte razliku između dva perioda
    razlika = abs(period_analitički - period_numerički)

    print(f"Za ∆t = {delta_t}, razlika između analitičkog i numeričkog perioda je {razlika}")

