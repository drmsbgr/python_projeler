from tkinter import *


def Quit(page: Tk):
    page.destroy()
    OpenLoginPanel()
    return


def OpenAccountPanel(name, password):
    page = Tk()
    page.title("Hesap Paneli")
    Label(page, text=f"KULLANICI ADI:\t{name}", padx=32, pady=32).grid(row=0, column=1)
    Label(page, text=f"ŞİFRE:\t{password}", padx=32, pady=32).grid(row=1, column=1)
    Button(page, text="Çıkış Yap", padx=32, pady=32, command=lambda: Quit(page)).grid(
        row=2, column=1
    )
    page.mainloop()


def Login(name, password, resultLabel, root):
    if name == "admin" and password == "123":
        print("giris yapildi")
        resultLabel["text"] = "SONUÇ: Giriş Başarılı!"
        root.destroy()
        OpenAccountPanel(name, password)
    else:
        print("giris basarısız")
        resultLabel["text"] = "SONUÇ: Giriş Başarısız!"


def OpenLoginPanel():
    root = Tk()
    root.title("Giriş Paneli")

    userNameField = _extracted_from_OpenLoginPanel_5(
        root, "Kullanıcı adınızı girin", 1
    )
    userPasswordField = _extracted_from_OpenLoginPanel_5(
        root, "Şifrenizi girin", 2
    )
    resultLabel = Label(root, text="", padx=10, pady=10)
    resultLabel.grid(row=4, column=1)

    loginButton = Button(
        root,
        text="Giriş Yap",
        padx=10,
        pady=10,
        command=lambda: Login(
            userNameField.get(), userPasswordField.get(), resultLabel, root
        ),
    )

    loginButton.grid(row=3, column=1)
    root.mainloop()


# TODO Rename this here and in `OpenLoginPanel`
def _extracted_from_OpenLoginPanel_5(root, text, row):
    Label(root, text=text, padx=10, pady=10).grid(row=row, column=0)
    result = Entry(root, width=30, borderwidth=5)
    result.grid(row=row, column=1)

    return result


OpenLoginPanel()
