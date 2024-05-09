A = input()
B = input()

if  (65 <= ord(A) <= 90) and (65 <= ord(B) <= 90):
    if abs(ord(A) + 26 - ord(B)) <= 13:
        print(ord(A) + 26 - ord(B))
    elif abs(ord(B) + 26 - ord(A)) <= 13:
        print(ord(B) + 26 - ord(A))
    else:
        print(abs(ord(A) - ord(B)))
else:
    print("Tidak valid")