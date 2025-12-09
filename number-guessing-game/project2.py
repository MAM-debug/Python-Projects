print("WELCOME TO THE NUMBER GUESSING GAME BRO!")
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please enter a number greater than 0")
        quit()
else:
    raise ValueError("please type a number next time")

random_number = random.randrange(top_of_range)
score = 0

while True:
    score += 1
    user_guess = input("make a guess bro: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess < 0 or user_guess >= top_of_range:
            print("please enter a number between 0 and " + str(top_of_range))
            continue
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you got it right bro")
        break
    elif user_guess > random_number:
        print("your guess is too high bro")
    elif user_guess < random_number:
        print("your guess is too low bro")

print("The number was: " + str(random_number))
print("you made ", score, " attempts to guess the number")
print("THANKS FOR PLAYING!")