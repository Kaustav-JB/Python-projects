from random import randint
from art import font

print(font)

easy = 10
hard = 5

print("Welcome to GUESS THE NUMBER game")

def level(select):
    if select == "easy":
        return easy
    elif select == "hard":
        return hard
    else:
        print("Invalid input")
        return level(input("Try again! Choose your difficulty.\n"))

def check_answer(guess,target,turns):
    if guess>target:
        if turns == 1:
            print("\nToo high.")
        else:
            print("\nToo high. Guess again!")
        return turns-1
    elif guess<target:
        if turns == 1:
            print("\nToo low.")
        else:
            print("\nToo low. Guess again!")
        return turns-1
    else:
        print("\nCongrats! You guessed the correct answer!")

def game():
    target = randint(1,100)
    select = input("\nSelect your level of difficulty : 'Easy' or 'Hard'\n").lower()
    turns = level(select)
    # print(f"The value is {target}")  #"This is the answer"
    guess = 0
    while guess!=target:
        print(f"\nYou have {turns} guess left")
        guess = int(input("Guess the number : "))
        turns = check_answer(guess,target,turns)
        if turns==0:
            print("\nGAME OVER!.\nYou are out of turns!")
            print(f"\nThe correct answer was {target}\n")
            return
    play_again = input("\nPress Y to play again!\nPress N to quit!\n").upper()
    if play_again.lower()=="y":
        game()
    else:
        print("\nThanks for playing!")
        return

game()
