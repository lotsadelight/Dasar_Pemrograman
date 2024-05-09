def quicksort(arr, low, high):
    if high > low:
        j = low - 1
        for i in range(low, high):
            if arr[i] < arr[high]:
                j += 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        (arr[j+1], arr[high]) = (arr[high], arr[j+1])
        quicksort(arr, low, j)
        quicksort(arr, j+2, high) 

array = [-1, -6, 7, 9, -8, 10, 30, -5]
quicksort(array, 0, 7)
print(array)
# 3, 4, 5, 7, 9, 7, 8
# high = 6
# low = 0 