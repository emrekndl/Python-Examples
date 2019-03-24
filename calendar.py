import datetime

takvim = [('Ocak', range(1, 31 + 1),'01'),
            ('Subat', range(1, 28 + 1,),'02'),
            ('Mart', range(1, 31 + 1),'03'),
            ('Nisan', range(1, 30 + 1),'04'),
            ('Mayis', range(1, 31 + 1),'05'),
            ('Haziran', range(1, 30 + 1),'06'),
            ('Temmuz', range(1, 31 + 1),'07'),
            ('Agustos', range(1, 31 + 1),'08'),
            ('Eylul', range(1, 30 + 1),'09'),
            ('Ekim', range(1, 31 + 1),'10'),
            ('Kasim', range(1, 30 + 1),'11'),
            ('Aralik', range(1, 31 + 1),'12')]

liste=dict()
hafta = ['Pa', 'Sa', 'Ca', 'Pe', 'Cu', 'Ct', 'Pa']

def goster():
 
    h = 0 
    print("\n")
    for ay, gunler, t in takvim:
        print('{0} {1}'.format(ay, 2018).center(20, ' '))
        print(''.join(['{0:<3}'.format(w) for w in hafta]))
        print('{0:<3}'.format('')*h, end='')
        
        for gun in gunler:
            print('{0:<3}'.format(gun), end='')
            h += 1
            if h == 7:
                print()
                h = 0 
        print('\n')
        
        for k,v in liste.items():
            g,a,y=v.split(".")
            if a==t:
                print(k," => ",v)
    print("\n")

    

def ekle():
    while 1:
        etkinlikAdi=input("\nEtkinlik ismini giriniz :")
        if etkinlikAdi in liste:                 #etkinlik.has_key(etkinlikAdi):
            print("Girdiginiz etkinlik ismi kullanilamaz!Yeni isin giriniz.")
        else:
            break
    while 1:
        try:
            tarih=input("\nTarihi giriniz(14-03-2018) :")    
            g,a,yil=tarih.split("-")
            datetime.date(int(yil),int(a),int(g))
        except ValueError as hata:
            print("Hata! :",hata,"\n")
        if yil!="2018": 
            print("Tarih degeri yanlis girildi!Gösterilen sekilde giriniz.(2018)")
        else:
            break
            
    yeniTarih=tarih.replace("-",".")
    liste[etkinlikAdi]=yeniTarih 
    if etkinlikAdi in liste:
        print("Etkinlik eklendi.\n")   

while 1:
    print("Etkinlik Takvimi")
    print("1-> Etkinlik Ekle\n2-> Etkinlikleri Goster\n(Cikmak icin :0)",end=" ")
    islem=input(" : ")
    if islem=="1":
        ekle()
    elif islem=="2":
        goster()
    elif islem=="0":
        break
    else:
        print("Yanlis deger girdiniz!")
