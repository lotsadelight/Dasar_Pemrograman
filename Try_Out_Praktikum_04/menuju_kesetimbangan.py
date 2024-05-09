def selisih(n, arr):
    max = int(4294967296)
    index = int(-1)

    for i in range(1, n):
        satu = int(0)
        dua = int(0)
        for j in range(0, i):
            satu += arr[j]
        for k in range(i, n):
            dua += arr[k]
        selisih = abs(satu - dua)
        if selisih < max:
            max = selisih 
            index = i    
    return(index)
            
n = int(input())
arr = list(map(int, input().split()))
print(selisih(n, arr))