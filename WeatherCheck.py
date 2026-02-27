weather = int(input("Enter the weather temperature: "))

if weather < 0:
    print("Freezing cold")
elif 0 <= weather <= 10:
    print("Very cold")
elif 11 <= weather <= 20:
    print("Cold")
elif 21 <= weather <= 30:
    print("Pleasant")
elif 31 <= weather <= 40:
    print("Hot")
else:
    print("Very hot")