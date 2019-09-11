from random import randint

rand_num = randint(1, 100)

def guess():
    print("Guess the number from 1 - 100!")
    try:
        num = int(input("Your number: "))
    except ValueError:
        print("Please input the correct value!")
        guess()
    if num > 100:
        print("Number out of range!")
        guess()
    if num > rand_num:
        print("Too big!")
        guess()
    elif num < rand_num:
        if num <= 0:
            print("Please input the number bigger then 0")
        else:
            print("Too small!")
        guess()
    else:
        print("You have guessed it!")

guess()