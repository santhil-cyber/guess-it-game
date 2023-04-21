import random
from art import logo
print(logo)

global number_choosed
number_choosed = random.randint(0, 100)
print("Welcome to the number guessing Game!!!\n Choose a Number between 1 to 100")
print(f"Number is {number_choosed}")

easy_level = 10
hard_level = 5
level = input("Choose a level of difficulty:- easy or hard ")
chance = True
counter = 0


def main():
    global counter, chance
    if level == "easy":
        number = int(input("guess a number:- "))
        counter = counter + 1
        if number == number_choosed:
            print("Congrats!!! You won")
        elif number_choosed > number:
            print("too low")
            print(f"You have {easy_level - counter} chance left")
        elif number_choosed < number:
            print("too high")
            print(f"You have {easy_level - counter} chance left")

        if counter == 10:
            print("You lost bud. Try again!!")
            chance = False

    elif level == "hard":
        number = int(input("guess a number:- "))
        counter = counter + 1
        if number == number_choosed:
            print("Congrats!!! You won")
        elif number_choosed > number:
            print("too low")
            print(f"You have {hard_level - counter} chance left")
        elif number_choosed < number:
            print("too high")
            print(f"You have {hard_level - counter} chance left")

        if counter == 5:
            print("You lost bud. Try again!!")
            chance = False
    if chance == False:
        play_again = input("Do you want to play again? y or n")
        if play_again == "y":
             print("Fine. just refresh the page")
        else:
            print("Bye!!!...see ya")




while (chance):
    main()
