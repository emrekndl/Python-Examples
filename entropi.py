#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import numpy as np

kanBasinclari = [120, 124, 200, 65, 101, 114, 116, 98, 154, 140, 120, 80,
                 165, 190, 166, 152, 135, 123, 143, 119, 111, 100, 147, 112,
                 154, 99, 178, 107, 97, 68, 122, 105, 99, 65, 154, 124]


def Frekans(liste):
    # return_conts=True frekans değerlerini veirir
    arr = np.unique(liste, return_counts=True)
    # arr[0] :array([1, 2]) dizi elemanları - arr[1] :array([1, 3]) frekansları
    return arr[1]/np.sum(arr[1], dtype=np.float)


# Entropi H(X) = -1*Ei(p(Xi)*log(p(Xi)))
def entropi(liste):
    # P her elemanin olasiligi(gorulme frekansi / toplam eleman sayisi)
    P = Frekans(liste)
    f = -1*P*np.log2(P)
    return np.sum(f)


def imageHistogram(img):
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    size_y = img1.shape[0]
    size_x = img1.shape[1]

    flattened = img1.reshape([size_x*size_y])  # düzleştirilmiş matris
    rhist, _, _ = plt.hist(flattened, bins=256)  # ,log=True)
    cv2.imshow("Goruntu", img)
    plt.title("Goruntu Histogrami")
    plt.show()


def imageEntropi(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # gri
    size_y = img.shape[0]
    size_x = img.shape[1]
    dMatris = img.reshape([size_x*size_y])  # düzleştirilmiş matris
    return entropi(dMatris)


def main():
    img = cv2.imread("../goruntuIsleme/images/maviTren.jpg")

    print("Kan Basınç Değerleri Entropisi :", entropi(kanBasinclari))
    plt.title("Kan Basinc Degerleri")
    #plt.scatter(kanBasinclari, kanBasinclari)
    plt.plot(kanBasinclari)
    plt.show()

    print("Fotoğraf Entropisi :", imageEntropi(img))

    imageHistogram(img)

if  __name__ == "__main__":
    main()
