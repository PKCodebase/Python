def sum(a,b):       #(Positional Argument)
    print("Sum is : ",a+b)
    # print(f"Sum is {a + b}")
sum(10,20)


print("------------------------")


def hello(name,age):       # Keyword Arguments
    print("Hello ",name," Your age is ",age)
hello("Ram",65)
hello(age=23,name="Ravi")



print("-------------------------")



def sub(a,b=10):    #Default Arguments
    print("Subtraction is : ",a-b)
sub(10)
sub(40,20)