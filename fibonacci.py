n = input("Fibonacci :")
t1=0
t2=1
for i in range(n):
    print(t2)
    s=t1+t2
    t1=t2
    t2=s
