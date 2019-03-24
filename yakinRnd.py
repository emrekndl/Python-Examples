#!/usr/bin/python

from random import random

liste = []
for i in range(100): # 1-0 arasinda rastgele deger iceren 100 elemanli liste olusturur
    liste.insert(i,random())

sayi1=0
sayi2=0
kucuk1=1
deger=0
for i in range(100):
    for j in range(100):
        if i==j or (i==sayi2 and j==sayi1): #ayni degerleri ve kontrol edilmis degerleri tekrar kontrol edilmesini engeller
            continue
        deger=abs(liste[i]-liste[j]) #sayilar arasindaki farklari bulur
        if deger<=kucuk1: #en kucuk fark  ve sayilar bulunur
            kucuk1=deger
            sayi1=i
            sayi2=j
        #print(liste[i]," - ",liste[j]," = ",liste[i]-liste[j])

#en yakin sayilar ve liste ekrana yazdirilir
print("\nEn yakin sayilar :",liste[sayi1]," - ",liste[sayi2]," = ",liste[sayi1]-liste[sayi2],"\n")
print("Liste:")
for i in liste:
    print(i)
