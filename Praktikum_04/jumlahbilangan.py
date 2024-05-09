x = int(input())
y = int(input())
sum = 0

for i in range(x, y+1):
    if i % 3 == 0 or i % 4 == 0:
        sum = sum + 1

if sum > 0:
    print(sum)
else: 
    print("Tidak Ada")