import string
def evaluate_password(password):
    length=len(password)>=8
    upper=any(char in string.ascii_uppercase for char in password)
    lower=any(char in string.ascii_lowercase for char in password)
    digit=any(char.isdigit() for char in password)
    special=any(char in string.punctuation for char in password)
    if length and upper and lower and digit and special:
        print("your passeord is strong!!")
    else:
        strength=[]
        if not length:
            strength.append("At least 8 charecyters long")
        if not upper:
            strength.append("At least one uppercase letter")
        if not lower:
            strength.append("At least one lowercase letter")
        if not digit:
            strength.append("At least one digit ")
        if not special:
            strength.append("At least one special character")
        print("Weak. "+",".join(strength))
        password=input("Enter your password: ")
        evaluate_password(password)
password=input("Eneter your password: ")
evaluate_password(password)