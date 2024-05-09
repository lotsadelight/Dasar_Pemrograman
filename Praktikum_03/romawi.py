romawi = dict([
    ("I", 1), 
    ("V", 5), 
    ("X", 10), 
    ("L", 50), 
    ("C", 100), 
    ("D", 500),  
    ("M", 1000)])

input = str(input())
length = len(input)
angka = [input[i] for i in range(length)]
sum = 0
i = 0

while i < length:
    if (length - i) > 1 and romawi[angka[i]] < romawi[angka[i+1]]:
        sum += (romawi[angka[i+1]] - romawi[angka[i]])
        i += 2
    else:
        sum = sum + (romawi[angka[i]])
        i += 1

print(sum)