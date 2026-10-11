count = 0
yol = 20000  # Başlangıç 20 km
for t in range(1, 41):  # Dakika 21–60
    yol += 1500  # Her dakika 1.5 km = 1500 m
    km = yol // 1000
    m = yol % 1000
    if km + m > 999:
        count += 1

print(count)