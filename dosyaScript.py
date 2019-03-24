#!/usr/bin/python3

dosya=open("odev.txt","r")  # odev.txt dosyasi okuma icin acilir

# sozluk yapilari baslangic degerleri ile olusturulur
universite={"soda":0,"ekmek":0,"su":0,"peynir":0,"sut":0}
merkez={"soda":0,"ekmek":0,"su":0,"peynir":0,"sut":0}
hastane={"soda":0,"ekmek":0,"su":0,"peynir":0,"sut":0}


for i in range(1000): # satir sayisi
    a=str(dosya.readline()) # her satiri tek tek a ya atar
    b=a.split("=>") # a stringini belirtilen karakter ile ikiye boler ve b listesine atar(b[0],b[1])
    c=b[1].split(" ") # b[1] deki stringi bosluk karakteri gecen yerlerinden 4 e boler
                      # ve c listesine atar(c[0,1,2,3])
    for j in range(4): # c listesinin karakterlerine erismek icin
        d=c[j].split(":") # c icindeki elemanlari : karakteri ile ikiye boler ve d listesine atar(d[0],d[1])
        if b[0] == "universite ": # a stringinin bolunmesi ile olusan b[0] elemanini kontrol eder
            universite[d[0]]=int(universite[d[0]])+int(d[1]) # universite sozlugu icindeki keylerin
        elif b[0]=="merkez ":                                # gosterdigi degeri yeni degerle toplar
            merkez[d[0]]=int(merkez[d[0]])+int(d[1]) # merkez sozlugu icindeki keylerin gosterdigi
        else: # elif b[0]=="hastane ":               # degeri yeni degerle toplar
            hastane[d[0]]=int(hastane[d[0]])+int(d[1]) # hastane sozlugu icindeki keylerin
                                                       #  gosterdigi degeri yeni degerle toplar   
# sozluk yapilarini ekrana yazdirir
print("Universite ={")
for (x,y) in universite.items():
    print(x,":",y)
print("}")
print("\nMerkez ={")
for (x,y) in merkez.items():
    print(x,":",y)
print("}")
print("\nHastane ={")
for (x,y) in hastane.items():
    print(x,":",y)
print("}")
