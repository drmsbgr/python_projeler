import os

os.system("cls")
a = input("ilk sayıyı gir\n->")
os.system("cls")
b = input("ikinci sayı gir\n->")
os.system("cls")
c = input("son sayıyı gir\n->")
os.system("cls")

a,b,c =int(a),int(b),int(c)
toplam = a+b+c
ortalama = float(toplam/3)

print("Toplam:",a,"+",b,"+",c,"=", toplam)
print("Ortalama:",toplam,"/ 3 =", "{00:.2f}".format(ortalama))