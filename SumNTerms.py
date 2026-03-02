n = int(input("Enter the number : "))
result = 0
for i in range(1,n+1):
    result += i
    print(result)

print("Without Loop")

result2 = n*(n+1)/2
print(result2)
