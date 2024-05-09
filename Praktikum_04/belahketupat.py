# Program BelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

def GambarBelahKetupat(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
#      sesuai spesifikasi soal
    for i in range(N):
        print("*", end="")
    

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
    if N > 0 and N % 2 == 1:
        return True
    else:
        return False

# ALGORITMA PROGRAM UTAMA gdplabs
N = int(input())
if (IsValid(N)):  # lengkapi dengan pemanggilan fungsi IsValid
    atas = (N // 2) + 1
    for i in range(atas):
        print(" " * (atas - i - 1), end="")
        GambarBelahKetupat(i * 2 + 1)
        print()
    for i in range(atas - 2, -1, -1):
        print(" " * (atas - i - 1), end ="")
        GambarBelahKetupat(i * 2 + 1)
        print()
            # lengkapi dengan pemanggilan prosedur GambarBelahKetupat
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")