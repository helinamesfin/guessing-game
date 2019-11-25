import random


number = random.randrange(1,11)
str_guess= input("What number do you think it is?")
guess= int(str_guess)

while guess != number:
    
    if guess > number:
        print("Not quite. Guess lower.")  
    elif guess < number:
        print("Not quite. Guess higher.")
    str_guess= input("What number do you think it is?")
    guess= int(str_guess)

if guess==number:
        print("Great job! You guessed right.")
    