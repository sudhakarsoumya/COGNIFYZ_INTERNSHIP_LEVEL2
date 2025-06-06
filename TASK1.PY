import random
print("\t\t\t\t Number Guessing Game")
print("\t\t\t\t-------------")
def guess_number():
    number=random.randint(1,100)
    while True:
        guess=int(input("Guess the number between 1 to 100:"))
        if guess==number:
            print("Congratulations! You guesses the correct ",number)
            break
        elif guess<number:
            print("Too Low! Try again")
        else:
            print("Too high! Try again")
    play_again=input("want to play again?(y/n):").lower()
    if play_again=='y':
        guess_number()
    else:
        print("Thank you playing!")
guess_number()