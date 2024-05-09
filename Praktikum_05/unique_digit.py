# Nama : Muhammad Ra'if Alkautsar
# NIM : 19623296

# PROGRAM UNIQUE DIGIT
# Program menerima sekumpulan bilangan yang akan disimpan dalam sebuah array dan akan berhenti menerima ketika pengguna memasukkan angka -9999. Bilangan dijamin lebih dari 0 dan valid. Keluarkan bilangan positif terkecil lebih dari 0 yang tidak terdapat pada array dan tidak dapat dibentuk dari penjumlahan dua elemen berbeda pada array.

masukan = 0
a = [int() for i in range(100)]
j = 0
while masukan != -9999:
    masukan = int(input())
    a[j] = masukan
    j += 1
i = 0
N = j
answer = False
while answer == False:
    kriteria_1 = False 
    kriteria_2 = True
    i += 1
    ketemu = False
    for p in range(0, N):
        if a[p] == i:
            ketemu = True 
    if ketemu == False:
        kriteria_1 = True
    for p in range(0, N):
        for q in range(0, p):
            hasil = a[p] + a[q]  
            if hasil == i:
                kriteria_2 = False
        for q in range(p+1, N):
            hasil = a[p] + a[q]
            if hasil == i:
                kriteria_2 = False

    if kriteria_1 == True and kriteria_2 == True:
        answer = True
        print(i)