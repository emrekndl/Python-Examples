
sayi1=int(input("ilk sayiyi giriiniz :"))
sayi2=int(input("ikinci sayiy giriniz :"))
sonuc=sayi1
i=0
j=0
while sonuc>=sayi2:

        sonuc=sonuc-sayi2
        i+=1
else: 
        sonuc*=10
        while sonuc>=sayi2:
            sonuc = sonuc - sayi2
            j+=1
            
            
            

print("sonuc:",i,j)
print("kalan :",sonuc)
