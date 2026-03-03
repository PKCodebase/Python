name = str(input("Enter the name : "))
reverse = ""
for i in range(len(name)-1,-1,-1):
    reverse += name[i];
print(reverse)
if(name==reverse):
    print("Palindrome")
else:
    print("Not Palindrome")