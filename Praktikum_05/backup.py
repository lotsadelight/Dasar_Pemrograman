# Nama : Muhammad Ra'if Alkautsar
# NIM : 19623296

# PROGRAM INCREASING ORDER

N = int(input())
a = list(map(int, input().strip().split()))
bisa = False
operasi = 0

for i in range(0, N):
    a_dup = [int() for i in range(N)]
    for j in range(0, N-1):
        if j != (N-1):
            a_dup[j+1] = a[j]
        else:
            a_dup[0] = a[j]
    a = a_dup
    operasi += 1
    tidaknaik = False
    for i in range(1, N):
        if a[i] > a[i-1]:
            tidaknaik = True
            bisa = True
    if tidaknaik == False: 
        print(operasi)
        break

if bisa == False:
    print("Tidak")