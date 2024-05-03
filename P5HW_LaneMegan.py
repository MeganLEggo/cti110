# Megan Lane

# 4/18/2024

# P5HW

# a math quiz that generates random numbers

# create the random numbers

import random
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
            
def option_1():
    count = 0
    print()
    print(f'     {n1}')
    print(f'+    {n2}')
    Pos_Total = n1 + n2
    answer = int(input("Enter answer. \n"))
    while answer != 'end':
        if Pos_Total == answer:
            count =+ 1
            print("Congradulations!")
            print(f"Number of guesses: {count}")
            answer = 'end'
            main_menu()
        elif Pos_Total < answer:
            count =+ 1
            print("Sorry, guess is too high.")
            answer = int(input("Try again. \n"))
        elif Pos_Total > answer:
            count =+ 1
            print("Sorry, guess is too low.")
            answer = int(input("Try again. \n"))
        else:
            count =+ 1
            print("Sorry, guess is wrong.")
            answer = int(input("Try again. \n"))

def option_2():
    count = 0
    print()
    print()
    print(f'     {n1}')
    print(f'-    {n2}')
    Neg_Total = n1 - n2
    answer = int(input("Enter answer. \n"))
    while answer != 'end':
        if Neg_Total == answer:
            count =+ 1
            print("Congradulations!!!! Your answer is correct.")
            print(f"Number of guesses: {count}")
            answer = 'end'
            main_menu()
        elif Neg_Total < answer:
            count =+ 1
            print("Sorry, guess is too high.")
            answer = int(input("Try again. \n"))
        elif Neg_Total > answer:
            count =+ 1
            print("Sorry, guess is too low.")
            answer = int(input("Try again. \n"))
        else:
            count =+ 1
            print("Sorry, guess is wrong.")
            answer = int(input("Try again. \n"))
            
def main_menu():
    print()
    print("MAIN MENU")
    print('-------------------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    enter = int(input("Please choose one of the menu options: "))
    while enter > 0:
        if enter == 1:
            option_1()
            enter = int(input("Please choose one of the menu options: "))
        elif enter == 2:
            option_2()
            enter = int(input("Please choose one of the menu options: "))
        elif enter == 3:
            enter = 0
            print('exit')
            print('Thank you for playing...')
            print('Bye!!')
            
def main():
    print("Welcome to Math Quiz")

            

main()


