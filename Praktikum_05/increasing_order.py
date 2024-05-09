# Nama : Muhammad Ra'if Alkautsar
# NIM : 19623296

# PROGRAM INCREASING ORDER

N = int(input())
a = list(map(int, input().strip().split()))
bisa = False
operasi = 0

for i in range(0, N-1):
    a_dup = [int() for i in range(N)]
    for j in range(0, N):
        if j != (N-1):
            a_dup[j+1] = a[j]
        else:
            a_dup[0] = a[j]
    a = a_dup
    operasi += 1
    naik = True
    penghitung = 1
    while naik == True and penghitung < N:
        if a[penghitung] < a[penghitung-1]:
            naik = False
        penghitung += 1
    if naik == True: 
        print(operasi)
        bisa = True
    else:
        bisa = False


if bisa == False:
    print("Tidak")