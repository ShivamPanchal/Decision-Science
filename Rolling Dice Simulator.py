#This is my first attempt at Python, Maybe other beginners will find it helpful?

import random

min=1
max=6

yes="y"
no="n"

dice1=random.randint(min,max)
dice2=random.randint(min,max)

user_input = input("Press Y to roll the Dice, N to exit ")

while user_input != no:
    if user_input == yes:
        dice1=random.randint(min,max)
        dice2=random.randint(min,max)
        print()
        print ("Dice have been rolled")
        print()
        print ("Your first Dice has a value of", dice1)
        print()
        print ("Your second Dice has a value of", dice2)
        print()
        print ("Value of both Dice = ", dice1 + dice2)
        print()
        user_input = input ("Roll the Dice again ? ")
    elif user_input == no:
        exit
