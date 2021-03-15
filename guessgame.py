def Guess_the_number_now():
    print()
    print('Hello User, welcome to guess the number game.\n')
    print('Rules are as follows:\nGuess a number\nThe computer will tell you if you have to go lower or higher to reach the number.')
    print('Best of luck')

def the_input_part():
    print("\n\nThe number to guess will be between 1 and 20")
    from random import randint
    nums_to_guess = randint(1,20)
    while True:
        enter_choice = int(input("Guess the number: "))
        if enter_choice < nums_to_guess:
            print("Guess higher")
        elif enter_choice > nums_to_guess:
            print("Guess lower")
        elif enter_choice == nums_to_guess:
            print('Congratulations!')
            the_input_part()
        else:
            pass
Guess_the_number_now()
the_input_part()