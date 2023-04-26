import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a==0:
    print('tidak ada akar')
else:
    D=b**2-4*a*c
    if D<0:
        print('akar imajiner')
    elif D>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print("x1 =", x1)
        print("x2 =", x2)
    else:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=x1
        print("x1 =", x1)
        print("x2 =", x2)
    
