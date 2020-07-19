import math

def f(x):
    return (12*x)-3*(x**4)-2*(x**6)

a = 0.75
b = 1
tol = 10**-5
i= 0
e = 0.0001
while(i<5):
    m = a +(b-a)/2
    if(f(m-e) < f(m+e)):
        b = m + e
    else:
        a = m - e
    print("a:", a,"b:",b,"m:",m)
    if abs(a-b) <= tol:
        print("m:",m)
        break
    i += 1