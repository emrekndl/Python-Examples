#!/usr/bin/python
import random


def loto(*tahmin):
    sayi = range(1,50)
    liste = []
    sayac=0
    liste = random.sample(sayi,6) # rastgele 6 numune sayi alinir.tutulan sayilarin benzer olmasini engeller
    for i in range(6): 
        for j in range(6): # tahmin edilen liste ile tutlan listeyi karsilastirir
            if liste[i] == tahmin[j]:
                sayac+=1
    #dogru tahminleri yazdirir
    print(sayac," sayi dogru tahmin ettiniz.")
    print("Tahmininiz :",end="")
    for i in tahmin:
        print(i,end=" ")
    print("\n  Tutulan  :",end="")
    for i in liste:
        print(i,end=" ")
    

loto(29,36,7,14,26,35)
