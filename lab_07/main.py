op = int(input("işlem seç kanka(giriş:1,kayıt ol:2,çıkış:3): "))


def login():
    name = input("kullanıcı adınızı girin: ")
    passw = input("şifrenizi girin: ")

    with open("account.txt", "r") as file:
        l = file.readline()
        l2 = l.split(",")

    if name == l2[0] and passw == l2[1]:
        print(f"Hoşgeldiniz {name}")
    else:
        print("önce kayıt ol brom")


def register():
    name = input("kullanıcı adınızı girin: ")
    passw = input("şifrenizi girin: ")

    with open("account.txt", "w") as acc:
        acc.write(f"{name},{passw}")


if op == 1:
    login()
elif op == 2:
    register()
