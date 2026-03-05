import  random

num = random.randint(1,10)
tries = 0
print("number : ", num)
while True:
    guess=int(input("Guess the number : "))


    if(num == guess):

        print("You are right : ")
        break
    elif num > guess:
        print("Please choose little bit higher")
        tries=tries+1
    elif num < guess:
        print("Please choose little bit smaller")
        tries=tries+1
    else:
        print("Please choose a number")
        tries=tries+1



