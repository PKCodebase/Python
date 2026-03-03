name = str(input("Enter a name:"))
reverse = ""
for i in range(len(name)-1,-1,-1):
    reverse = reverse + name[i]
print(reverse)