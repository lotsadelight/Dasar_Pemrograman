# Menerima input
n = int(input())
arr = list(map(int, input().split()))

# Proses
dict = {}
for i in range(0, n):
    if arr[i] not in dict:
        dict[arr[i]] = 1
    else:
        dict[arr[i]] += 1

mode = 0
value = 0
for i in dict:
    if dict[i] > value:
        value = dict[i]
        mode = i
    elif dict[i] == value and i < mode:
        value = dict[i]
        mode = i

print(mode) 