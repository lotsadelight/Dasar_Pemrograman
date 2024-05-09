N = int(input())
if N <= 0 or N > 100:
    print("Tidak valid")
else:
    a = list(map(int, input("").split()))
    x = int(input())
    for i in range(N-1):
        swapped = False
        for j in range(0, N-i-1):
            if a[j] > a[j + 1]:
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if swapped == False:
            break

    batasbawah = 0
    while batasbawah < N and a[batasbawah] <= x:
        batasbawah += 1

    if batasbawah >= N-1:
        print(-1)
    else:
        print(a[batasbawah+1])