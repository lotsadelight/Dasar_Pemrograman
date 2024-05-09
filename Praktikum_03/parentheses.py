string = str(input())
array = [string[i] for i in range(len(string))]
stack = []
opening = ['(', '[', '{']
closing = [')', ']', '}']
pasangan = {'(': ')', '[': ']', '{': '}'}
status = True

for i in array:
    if i in opening:
        stack.append(i)
    elif i in closing: 
        if len(stack) == 0:
            status = False
            break
        bracket_terakhir = stack.pop()
        if pasangan[bracket_terakhir] != i:
            status = False
            break

if status == True and len(stack) == 0:
    print("valid")
else:
    print("tidak valid")