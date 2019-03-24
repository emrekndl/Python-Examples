#!/usr/bin/python
import random

 # buyuk harfler 65-90
 # kucuk harfler 97-122
 # rakam 48-57
 # karakter

karakter = ['!','%','?','*','#']
liste = list()

#ranstgele bir karakter olusturur ve geri dondurur
def rnd():
    r = random.randint(1,4)
    if r==1:
         return chr(random.randint(97,122)) #rastgele kucuk harf olusturur
    elif r==2:
        return chr(random.randint(48,57)) #rastgele rakam olusturur
    elif r==3:
        return karakter[random.randint(0,4)]  #rastgele belirtilen karakterler olusturur
    else:
        return chr(random.randint(65,90)) #rastgele buyuk harf olusturur

#rastgele karakterler kullanarak 8 karakterlik paralo olusturup listeye atar
def prlOlustur(liste):
    for i in range(100):
        passwd = []
        for j in range(8):
            passwd.insert(j,rnd()) #rastgele gelen karakteri passwd listesine atar
        liste.insert(i,"".join(passwd)) #passwd listesindeki paralolari string tipinde listeye atar
        del passwd

#paralo listesindeki yan yana gelen rakamlari bulup yazdirir
def hataRakam(liste):
    for i in range(100):
        for j in range(8):
            if liste[i][j].isdigit(): #paralo listesindeki  paralolarin karakterlerini sirayla sayi olup olamdigini kontrol eder
                if j<7: # paralo boyutunu asmammasını onler
                    if liste[i][j+1].isdigit(): # paralonun sayi olan karakterinden sonraki karakterin sayi olup olmadigini kontrol eder
                        print("Hata! (rakam tekrarli) :"+liste[i])
	                #break		
                elif j==7:
		      if liste[i][j-1].isdigit():
			  print("Hata! (rakam tekrarli) :"+liste[i])
			    

prlOlustur(liste)

#paralo listesini yazdirir
for i in liste:
    print(i,end="\n")

hataRakam(liste)
