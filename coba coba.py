
a = 1
angka = 1
batas = int(input("masukan batas = "))
print("+-------+----------+")
print("| Angka |  Kuadrat |")
print("+-------+----------+")
while a <= batas:
    b = angka*angka
    print("|", a, "    |",   b,  "      |")
    print("+-------+----------+")
    angka += 1
    a += 1
