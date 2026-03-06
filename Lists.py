a = [10,10,20,32,24,"name",True,print()]
print(a)
print(a[0:5])  #Slice

print(a[-1])
print(a[-2])

print("--------------------------------------")

arr = [10,20,23,24,34,40]
# 1st  way using index
for i in range (len(arr)):
    print(arr[i])

# 2nd way Directly on values

print("-----------------------------")

for i in arr:
    print(i)