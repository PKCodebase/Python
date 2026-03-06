# lst = [10,34,20,21,35,89]
lst = list(map(int,input("Enter the numbers :").split(",")))
val = True

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        val = False
        break

if val:
    print("Sorted")
else:
    print("Not Sorted")