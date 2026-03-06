list = [10,30,43,23,45,67]
largest = list[0]
index = 0
for i in range(len(list)):
   if(list[i] >largest):
       largest = list[i]
       index = i
print(largest,index)

