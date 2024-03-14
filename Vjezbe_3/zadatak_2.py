def zbrajanje(N):
    x = 5
    for i in range(N):
        x += 1/3
    for o in range(N):
        x -= 1/3
    return x

niz_N = [200, 2000, 20000]

for N in niz_N:
    print("Rezultat za {} zbrajanja je: {:.10f}".format(N, zbrajanje(N)))
