def getDigitCount(x):
    c = 0

    while x >= 1:
        c += 1
        x /= 10
    return c


def getDigit(x, i):
    p = getDigitCount(x) - i - 1
    return int(((x - (x % (10**p))) / (10**p)) % 10)


def isValid(no):
    s10 = sum(getDigit(no, i) * ((-1) ** i) * (7 ** (1 - i % 2)) for i in range(9)) % 10
    s11 = sum(getDigit(no, i) for i in range(10)) % 10

    return (
        getDigitCount(no) == 11
        and no % 2 == 0
        and getDigit(no, 0) != 0
        and s10 == getDigit(no, 9)
        and s11 == getDigit(no, 10)
    )


no = int(input("tc gir\n->"))

print(isValid(no))
