number = int(input("Enter the number : "))
sum = 0
for i in range(1,number):
    if number % i == 0:
        sum +=i;
print(sum)
if sum == number:
    print("Perfect")
else:
    print("Not perfect")
