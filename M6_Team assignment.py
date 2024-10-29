# David Ramirez
# 10/29/2024

import random

Anw = int(input("Please guess a number between 1 and 10: "))
random_number = random.randrange(1,10)

while Anw > random_number:
    print(f"Please guess lower")
    Anw = int(input("Please guess a number between 1 and 10: "))
while Anw < random_number:
    print(f"Please guess higher")
    Anw = int(input("Please guess a number between 1 and 10: "))

if Anw == random_number:
    print("Well done, you guessed it")

#This program creates a random number for the user and loops until the user gets "Well done, you gussed it"