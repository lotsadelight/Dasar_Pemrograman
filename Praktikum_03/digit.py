digit = [0 for i in range(0, 10)]
num = 0

while num < 100:
    bil = int(input())
    if bil < 0:
        break
    else:
        num += 1
        while True:
            i = bil % 10
            digit[i] += 1
            if (bil // 10) == 0:
                break
            else:
                bil //= 10

print(num)
for i in range(0, 10):
    if digit[i] != 0:
        print("%i" % i, end="")
        print(" : ", end="")
        print("%i" % digit[i])