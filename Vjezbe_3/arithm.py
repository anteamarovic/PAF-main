#a) bez gotovih modula
import numpy as np
import matplotlib.pyplot as plt
import math

#prvo moramo definirati listu tocaka
tocke = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#sada racunamo artitemticku sredinu
aritmeticka_sredina = sum(tocke) / len(tocke)
print(aritmeticka_sredina)

#standarnda devijacija
suma = 0
tocke2= [2, 4, 5, 7, 9, 10, 11, 13, 14, 15]
a_sredina= sum(tocke2) / sum(tocke2)
for el in tocke:
    a = (el-a_sredina)**2
    suma+=a
s = (suma)/len(tocke2)
standarnda = math.sqrt(s)
print(standarnda)

