N = int(input())
a = list(map(int, input().strip().split()))

smallestDiff = 9999999999999999999
for i in range(0, N):
    for j in range(0, N):
        selisih = abs(a[i] - a[j])
        if selisih != 0 and selisih < smallestDiff:
            smallestDiff = selisih

if smallestDiff == 9999999999999999999:
    print(0)
else:
    print(smallestDiff)
