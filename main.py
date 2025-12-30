import art
import random
print(art.logo)

print("Welcome to the Number Guessing Game !")
print("I am thinking of a Nubeer between 1 and 100")
mode=input("Choose a difficulty. Type 'easy' or 'hard':").lower()

computer_number=random.randint(1,100)

if mode=="easy":
    attempt=10
else:
    attempt=5

while attempt>0:
    print(f"{attempt} attempts left")
    user_guess=int(input("Guess the number"))
    if user_guess==computer_number:
        print("you guessed the number")
        break
    elif user_guess<computer_number:
        print("Too low")
    elif user_guess>computer_number:
        print("Too high")

    attempt-=1

if attempt==0:
    print("You lose")