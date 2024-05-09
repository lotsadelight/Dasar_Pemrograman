ketemu = False
s = str(input())

if len(s) > 6:
    for i in range(0, len(s)-6):
        if s[i] == "1":
            print("yes")
            ketemu = True
            break

if ketemu == False:
    print("no")