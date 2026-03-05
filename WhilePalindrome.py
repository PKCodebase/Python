numbers= int(input("Enter the number : "))
original = numbers
rev = 0
while numbers > 0:
    rev = rev*10 + numbers%10
    numbers = numbers//10
if original==rev:
        print("The number is palindrome")
else:
        print("The number is not palindrome")
