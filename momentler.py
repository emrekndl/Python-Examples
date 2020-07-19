#!/usr/bin/env python3

from math import sqrt


kanBasinclari = [120, 124, 200, 65, 101, 114, 116, 98, 154, 140, 120, 80,
                 165, 190, 166, 152, 135, 123, 143, 119, 111, 100, 147, 112,
                 154, 99, 178, 107, 97, 68, 122, 105, 99, 65, 154, 124]


def aritmetikOrtalama(liste):
    n = len(liste)
    t = 0
    for i in liste:
        t += i
    return (t/n)


# Standart Sapma(S)
def standartSapma(liste):
    aOrtalama = float(aritmetikOrtalama(liste))
    t = 0
    for i in liste:
        t += ((i - aOrtalama)**2)
    n = len(liste)
    return sqrt(t/(n-1))


# Mk = (Ei,n(Xi-X)**k)/n
def momentK(liste, k):
    aOrtalama = float(aritmetikOrtalama(liste))
    n = float(len(liste))
    t = 0
    for i in liste:
        t += ((i - aOrtalama)**k)
    return t/n


# 4.Standart Moment = M4/(S**4) (kurtosis)
# 3.Standart Moment = M3/(S**3) (skewness)
def standartMomentler(liste, k):
    moment = float(momentK(liste, k))
    ss = float(standartSapma(liste))**k
    return moment/ss


print("Kan Basınçları :", kanBasinclari)
print("ELeman Sayısı :", len(kanBasinclari))
print("En Küçük Eleman :", min(kanBasinclari))
print("En Büyük Eleman :", max(kanBasinclari))
print("Aritmetik Ortalama :", aritmetikOrtalama(kanBasinclari))
print("Standart Sapma :", standartSapma(kanBasinclari))
print("3.Standart Moment :", standartMomentler(kanBasinclari, 3))
print("4.Standart Moment :", standartMomentler(kanBasinclari, 4))
