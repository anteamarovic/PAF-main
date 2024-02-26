def pravac(x3, y3, x4, y4):
    if x4 - x3 == 0:
        print("Vertikalna linija, x = {}".format(x3))
        return None
    
    a = (y4 - y3) / (x4 - x3)
    b = y4 - x4 * a
    return a, b

koeficijenti = pravac(3, 3, 3, 3)

if koeficijenti is not None:
    a, b = koeficijenti

    if a == 0:
        print('y = {}'.format(b))
    elif b == 0:
        print('y = {}x'.format(a))
    elif b < 0:
        print('y = {}x {}'.format(a, b))
    else:
        print('y = {}x + {}'.format(a, b))
