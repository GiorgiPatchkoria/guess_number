from random import randrange
import math



def main():
    choosing_game = int(input('Choose game \nUser to guess the number, Press 1 \nComputer to guess the number, Press 2 \n'))
    min_number = int(input('Enter minimum number: '))
    max_number = int(input('Enter maximum number: '))
    if choosing_game == 1:
        guess_number_user(min_number, max_number)
    elif choosing_game == 2:
        guess_number_computer(min_number, max_number)

def guess_number_user(min_number, max_number):
    random_number = randrange(min_number, max_number)
    attempt = 0
    user_number = math.inf
    while user_number != random_number:
        try:
            attempt += 1
            user_number = int(input('Choose number: '))
    
            if user_number > random_number:
                print('Your number is higher than random number')  
            elif user_number < random_number:
                print('Your number is lower than random number')
        except (ValueError, TypeError):
            print('Please write only numbers, try again')
            guess_number_user(min_number, max_number)

    print(f'Congrats, you guessed number in {attempt} attempt')

    game_over = input('Do you want to continue game? Yes or No, Y/N ')
    if game_over == 'Y':
        main()
    else: 
        pass

def guess_number_computer(min_number, max_number):
    computer_number = math.inf
    answer = ''
    attempt = 0
    while answer != 'c':
        attempt += 1
        computer_number = randrange(min_number, max_number)
        answer = input(f"Is {computer_number} correct (c), too low (l) or too high (h): ")
        if answer == 'l':
            min_number = computer_number + 1
        elif answer == 'h':
            max_number = computer_number - 1
        if min_number == max_number:
            attempt += 1
            print(f'Only number left is {min_number}\n')
            computer_number = min_number
            break

    print(f'Computer guessed number in {attempt} attempts')

    game_over = input('Do you want to continue game? Yes or No, Y/N ')
    if game_over == 'Y':
        main()
    else: 
      pass

main()