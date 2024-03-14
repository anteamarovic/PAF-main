#zadatak a)
a=5.0
b=4.935
print(a-b)
#Ocekujem rezultat '0.065', a dobivam rezultat '0.06500000000000039', mi ljudi koristimo dekadski brojevni sustav 
#dok racunala koriste binarni brojevni sustav(tj. imaju samo stanja 0 i 1) zbog toga racunala ne mogu zapisati odredene brojeve(npr.0.1,0.2,...)
#te nastaju aproksimacije i pogreske

#zadatak b)
a=0.1
b=0.2
c=0.3
suma= a+b+c
if b==0.6:
    print('rezultat iznosi 0.6')
else:
    print(suma)