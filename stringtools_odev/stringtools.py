ALPHABET = "abcçdefgğhıijklmnoöprsştuüvyz"


def reverse(s):
    return s[::-1]


def mirror(s):
    return s + reverse(s)


def remove_letter(letter, s):
    return s.replace(letter, "")


def is_palindrome(s):
    isPalindrome = True

    i = 0

    while i < len(s):
        if s[i] != s[len(s) - i - 1]:
            isPalindrome = False
            break
        i += 1

    return isPalindrome


def count(subs, s):
    i = 0
    c = 0

    while i <= len(s) - len(subs):
        c_s = "".join(s[i + j] for j in range(len(subs)))
        if c_s == subs:
            c += 1
        i += 1

    return c


def remove(subs, s):
    i = 0
    res = ""

    while i <= len(s) - len(subs):
        if s[i : i + len(subs)] == subs:
            res = s[:i] + s[i + len(subs) :]
            break
        i += 1
    return res


def remove_all(subs, s):
    i = 0
    res = s

    while i <= len(res) - len(subs):
        if res[i : i + len(subs)] == subs:
            res = res[:i] + res[i + len(subs) :]
            i = 0
        i += 1
    return res


def get_count_of_alphabet_letters(s: str):
    countlist = [0 for _ in ALPHABET]

    s = s.lower()

    for l1 in s:
        for l2 in ALPHABET:
            if l1 == l2:
                countlist[ALPHABET.index(l2)] += 1

    return countlist

def is_lower(ch):
    return ch in ALPHABET