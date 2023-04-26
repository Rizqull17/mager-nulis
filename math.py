import math
# input koefisien dari keyboard
a = float(input('Masukan a:'))
b = float(input('Masukan b:'))
c = float(input('Masukan c:'))
# hitung diskriminan d
d = (b**2)-(4*a*c)
print(d)
# menemukan x1 dan x2
x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)
print('Solusinya adalah{0}dan{1}'.format(x1, x2))
