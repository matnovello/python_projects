import random

print("working")

number = random.randint(1, 100)
x = int(input("guess a number" + " "))

while number != x:
    if x < number:
        # print("you guessed" + x + ", thats too low")
        print(f"you guessed {x}, which is too low... try again")
    elif x > number:
        # print("you guessed" + x + ", thats too high")
        print(f"you guessed {x}, which is too high... try again")
    else:
        #
        print(f"you guessed {x}, which is equal to {number}")
