#!/usr/bin/python

from random import randint

liste = []
sozluk = dict()
for i in range(100): #1-9 arasinda rastgele deger içeren 100 elamanli liste olusturur
    liste.insert(i,randint(1,9))

for i in range(1,10):
    sayac=0
    for j in range(100):
        if liste[j] == i: #ayni olan rakamlari kontrol eder ve sayac degerini artirir
            sayac+=1
    sozluk[str(i)]=sayac #ayni olan rakam sayilarini sozluğe atar

#liste ve sozluk yazdirilir
print(liste)
print("\n Sirali :")
for i in range(1,10):
    print(i," : ",sozluk[str(i)])
print("\n",sozluk)
