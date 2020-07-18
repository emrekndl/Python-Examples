import  time

def hesapla():
    sonuc = []
    for i in range(1000000): #  10
        #  time.sleep(.5)
        sonuc.append(i**4)

    return sonuc

def hesapla2():
    for i in range(1000000): #  10
        #  time.sleep(.5)
        yield  i**4

t1 = time.perf_counter()
s1 = hesapla()
t2 = time.perf_counter()
print(f"liste çalışma süresi : {t2-t1} sn")

t1 = time.perf_counter()
s2 = hesapla2()
t2 = time.perf_counter()
print(f"yield çalışma süresi : {t2-t1} sn")

print("liste kullanımı: ")
#print(hesapla())

print("yield kullanımı: ")
#for s in hesapla2():
#    print(s)

hGen =  hesapla2()
print(type(hGen))
print("generator next kullanımı :")
#  print(dir(hesapla2()))
for s in range(10):
    print(f"next{s+1}: {next(hGen)}")
