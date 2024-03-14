import stringtools

# girdi = input("Bir metin giriniz: ")
girdi = "Mississippi"

print(f"4.harf ve sonrası: {girdi[3:]}")

print(f"Metnin tersi: {stringtools.reverse(girdi)}")
print(f"Metnin ayna görüntüsü: {stringtools.mirror(girdi)}")
print(f"'e' harfleri olmadan metin: {stringtools.remove_letter('e',girdi)}")
print(f"Metin Palindromik mi?: {stringtools.is_palindrome(girdi)}")
print(f"Metinde 'is' alt metin adeti kaç?: {stringtools.count('is',girdi)}")
print(f"Metinden ilk 'iss' metninin silinmesi: {stringtools.remove('iss',girdi)}")
print(
    f"Metinden tüm 'iss' metinlerinin silinmesi: {stringtools.remove_all('iss',girdi)}"
)
