import pandas as pd


def loadData():
    df = pd.read_excel("students.xlsx")
    # df.set_index("No", inplace=True)
    return df


def listData():
    for row in loadData().values:
        print(row)


def saveData(df: pd.DataFrame):
    df.to_excel("students.xlsx", index=True)


def createData():
    no = int(input("öğrenci no girin: "))
    fname = input("ad girin: ")
    lname = input("soyad girin: ")
    midterm = int(input("vize notu girin: "))
    final = int(input("final notu girin: "))
    df = loadData()
    df.loc[len(df.index)] = [no, fname, lname, midterm, final]
    saveData(df)
    listData()


def deleteData():
    listData()

    df = loadData()

    selectedNo = int(input("silinecek öğrencinin indisini girin: "))
    df.drop(selectedNo, axis=0, inplace=True)
    saveData(df)
    listData()


def selectOp():
    op = int(input("işlem seç(1:listele,2:ekle,3:sil)"))

    if op == 1:
        listData()
        selectOp()
    elif op == 2:
        createData()
        selectOp()
    elif op == 3:
        deleteData()
        selectOp()


selectOp()
