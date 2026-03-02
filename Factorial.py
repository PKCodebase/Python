from math import factorial

number = int(input("Enter a number : "))

if number < 0:
    print("You provided a wrong number.")
else:
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    print(factorial)