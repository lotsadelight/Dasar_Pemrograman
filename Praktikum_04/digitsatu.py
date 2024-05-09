N = int(input())
a = list(map(int, input("").split()))
operasi = 0
for i in range(N):
    while a[i] >= 10:
        angka = a[i]
        sum = 0
        while angka > 0:
            sum += (angka % 10)
            angka //= 10
        a[i] = sum
        operasi += 1

print(operasi)