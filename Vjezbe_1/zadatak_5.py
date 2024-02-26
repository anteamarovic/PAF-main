import matplotlib.pyplot as plt

def pravac(x3, y3, x4, y4, boja='b', stil='-'):
    x_values = [x3, x4]
    y_values = [y3, y4]
    s = plt.plot(x_values, y_values, color=boja, linestyle=stil)
    
    opcija = input('Želite li spremiti graf kao PDF? (da/ne): ')
    
    if opcija.lower() == 'da':
        plt.savefig('zadatak_5.pdf')
        print('Graf spremljen kao PDF.')
    else:
        plt.show()
        print('Graf prikazan na ekranu.')
    
    return s

# Primjer poziva funkcije s mogućnošću specificiranja boje i stila
pravac(2, 4, 6, 8, boja='r', stil='--')
