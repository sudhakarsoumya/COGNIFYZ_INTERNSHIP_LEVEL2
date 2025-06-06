print("\t\t\t\t Fibonacci Seqence Generator")
print("\t\t\t\t------------")
def fibonacci_seq(terms):
    fibonacci_sequence=[0,1]
    for i in range(2,terms):
        next_term=fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence
while True:
    terms=int(input("Enter the number of terms for the fibonacci sequence:"))
    if terms<=0:
        print("Please enter a positive number")
        continue
    else:
        fib_sequence=fibonacci_seq(terms)
        print("Fibonacci sequence up to",terms,"terms : ",*fib_sequence)
        again=input("Do you want to calculate again?(y/n):").lower()
        if again=='y':
            continue
        else:
            print("Thank you for using our Fibonacci Generator")
            break