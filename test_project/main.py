def girilen_sayilari_topla():
    a = input("sayı gir\n->")
    b = input("sayı gir\n->")
    a = int(a)
    b = int(b)
    sum = a + b
    print(a, "+", b, "=", sum)


def girilen_sayilari_carp():
    a = input("sayı gir\n->")
    b = input("sayı gir\n->")
    a = int(a)
    b = int(b)
    carpim = a * b
    print(a, "*", b, "=", carpim)


def n_e_kadar_topla():
    n = input("hedef sayıyı giriniz\n->")
    n = int(n)
    toplam = 0
    for i in range(1, n + 1):
        toplam += i
    print("[1, ", n, "] arası toplam =", toplam)


op = input("İşlem seç\n(1->toplama, 2->carpma, 3->n'e kadar topla)\n->")
op = int(op)

if op == 1:
    girilen_sayilari_topla()
elif op == 2:
    girilen_sayilari_carp()
elif op == 3:
    n_e_kadar_topla()
else:
    print("Beklenmeyen bir değer girdiniz!")
