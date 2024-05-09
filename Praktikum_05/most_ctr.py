N = int(input())
a = list(map(int, input().strip().split()))


def quicksort(arr, low, high):
    if high > low: 
        j = low-1
        for i in range(low, high):
            if arr[i] < arr[high]:
                j += 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        (arr[high], arr[j+1]) = (arr[j+1], arr[high])
        quicksort(arr, low, j)
        quicksort(arr, j+2, high)
quicksort(a, 0, N-1)


modus = 0
penghitung = 0
current_number = int()
mode_number = int()

for i in range(0, N):
    if a[i] == current_number:
        penghitung += 1
    else: 
        current_number = a[i]
        penghitung = 1
    
    if penghitung > modus:
        mode_number = current_number
        modus = penghitung

print(mode_number)



