import random

def roll_dice():
    return random.randint(1, 6)
def game():
    total = 0

    while total < 100:
        command = input("Enter roll or bank: ")

        if command == "roll":
            number = roll_dice()
            print("Dice:", number)

            if number == 1:
                print("You rolled a 1! You get a zero for this round! ")
                total = 0
            else:
                total += number
                print("total:", total)

        elif command == "bank":
            print("Banked total:", total)
            break

        else:
            print("gwdhbwsds")        
    if total >= 100:
        print("You win!")

game()
