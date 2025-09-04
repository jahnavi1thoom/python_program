def checkCharacter(n):
    if n.isalpha():
        return "Alphabet"
    elif n.isdigit():
        return "Digit"
    else:
        return "Special Character"
n=input("enter any character:")
print(checkCharacter(n))