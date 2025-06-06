import random
print("\t\t\t\t Number Gusser")
print("\t\t\t\t---------------")
def feedback(guess,number,min_num,max_num):
    range_size=max_num-min_num
    if abs(guess-number)>range_size*0.2:
        if guess<number:
            print("Too low! Try again")
        else:
            print("Too high! Try again")
    else:
        print("low! try again"if guess<number else "high! Try again")
def guess_the_number(min_num,max_num):
    number= random.randint(min_num,max_num)
    while True:
        guess=int(input(f"Guess the number between {min_num}and{max_num}:"))
        if guess==number:
            print("congratulations !! You guesses the correct number ",number)
        break
    else:
        feedback(guess,number,min_num,max_num)
    play_again=input("wanna play again?(y/n):").lower()
    if play_again=='y':
        guess_the_number(min_num,max_num)
    else:
        print("Thank you for playing!")
min_range=int(input("Enter the minimum number in the range:"))
max_range=int(input("Enter the maximum number in the range:"))
guess_the_number(min_range,max_range)