n = int(input())
x = int(input())
a = list(map(int, input("").split()))
ketemu = False

for i in range(0, n):
    if a[i] == x:
        print(a[i])
        ketemu = True
        break

smallest = a[0]
selisih_smallest = abs(a[0] - x)
for i in range(1, n):
    selisih = abs(a[i]-x)
    if selisih != 0 and selisih < selisih_smallest:
        selisih_smallest = selisih
        smallest = a[i]

biggest = a[0]
selisih_biggest = abs(a[0] - x)
for i in range(1, n):
    selisih = abs(a[i]-x)
    if selisih > selisih_biggest:
        selisih_biggest = selisih
        biggest = a[i]

if ketemu == False:
    print("TIDAK ADA")
print(smallest)
print(biggest)
