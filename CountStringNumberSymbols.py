value = str(input("Enter the value :"))
letter = 0
numbers = 0
symbols = 0
spaces = 0

for ch in value:
    if ch == " ":
        spaces += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letter += 1
    elif ch >= '0' and ch <= '9':
        numbers += 1
    else:
        symbols += 1
print(letter)
print(numbers)
print(symbols)
print(spaces)