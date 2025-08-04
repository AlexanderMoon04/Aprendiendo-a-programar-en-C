#import random #This brings all the functions of the module
from random import choice,randint,shuffle
from statistics import mean
from sys import argv,exit #argv list all of the words typed in the .py
#Random library
coin = choice(["Heads", "Tails"])
print(f"{coin}\n")

number = randint(1,10)
print(f"{number}\n")

cards = ["Jack", "Queen", "King","Joker","As"]
shuffle(cards)
for card in cards:
    print(card)
print()

#statics library
print(f"Average: {mean([10,5,6,2,9])}\n")
 
#sys library
#Check for errors
if len(argv) < 2:
    exit("Too few arguments")

#Print name tags
for arg in argv[1:]:
    print("Hello, my name is ", arg) #argv [0] = name of the program (name.py)
