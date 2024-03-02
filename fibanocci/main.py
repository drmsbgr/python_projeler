import os

os.system("cls")

n = int(input("terim sayısını giriniz\n->"))

num1 = 0
num2 = 1

s = ""

for i in range(0, n):
    s += f"{num1}, "
    nextNum = num1 + num2
    num1 = num2
    num2 = nextNum

print(s)
