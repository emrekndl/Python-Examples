a = input("ilk araligi giriniz :")
b = input("ikinci araligi giriniz :")
print("Asal Sayilar :")
for i in range(a,b+1):
    sayac=0
    for j in range(2,i):
        if i%j==0:
            sayac=1
    if sayac==0:
        print(i)
