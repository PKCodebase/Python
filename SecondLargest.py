

l = [23,54,67,43,27,98]
large = l[0]
secondLargest = l[0]

for i in range(len(l)):
    if(l[i]>large):
        secondLargest = large
        large = l[i]

print(large)
print(secondLargest)