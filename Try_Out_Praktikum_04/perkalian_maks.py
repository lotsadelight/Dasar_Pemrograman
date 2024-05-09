###

# Menerima input
a = int(input())
an = list(map(int, input().split()))
b = int(input())
bn = list(map(int, input().split()))

# Proses
value = 0
for i in range(0, a):
    for j in range(0,b):
        result = an[i] * bn[j]
        if result > value:
            value = result

print(value)

###