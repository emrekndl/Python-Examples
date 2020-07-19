import math

def f(x):
    return math.sin(x)-x**2

a =0
b =1
r = (math.sqrt(5)-1)/2
x1 = a + (b-a)*r
x2 = b - (b-a)*r
print("r:",r)
print("x1:",x1)
print("x2:",x2)
f1 = f(x1)
f2 = f(x2)
i=0
print("")
while(i<5):
    if(f1 > f2):
        a = x2;
        x2=x1;
        x1 = a + (b-a)*r
        f1 = float(f(x1))

    else:
        b = x1;
        x1 = x2;
        x1 = b - (b - a) * r
        f2 = float(f(x2))

    print("f1:%.2f" % round(f1,2),"f2:%.2f" % round(f2,2), "x1:%.2f" % round(x1,2), "x2:%.2f" % round(x2,2))
    i += 1
