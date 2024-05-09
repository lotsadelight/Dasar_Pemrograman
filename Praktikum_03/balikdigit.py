negatif = False
angka = int(input())
if angka < 0:
    negatif = True
    angka *= -1

dup_angka = angka
panjang = 0
sum = 0

while dup_angka != 0:
    dup_angka //= 10
    panjang += 1
    
while panjang != 0:
    sum += ((angka % 10) * 10**(panjang-1))
    angka //= 10
    panjang -= 1

if negatif == True: 
    sum *= -1

print(sum)