N = int(input())
M = int(input())

segitiga = [[] for k in range(N)]
for i in range(N):
    baris = [0] * (i + 1) 
    for j in range(i + 1):
        if j == 0 or j == i:
            baris[j] = M
        else:
            if i > 0: 
                baris[j] = segitiga[i - 1][j - 1] + segitiga[i - 1][j]
            else:
                baris[j] = M
    segitiga[i] = baris

for baris in segitiga:
        print(" ".join(map(str, baris)))