def print_rhombus(rows):
    # Upper part of the rhombus
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (i * 2 + 1))

    # Lower part of the rhombus
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + "*" * (i * 2 + 1))

rows = int(input("Enter the number of rows for the rhombus: "))
print_rhombus(rows)