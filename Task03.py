import re

def passwordchecker(password):

    length = len(password) >= 8

    uppercase = bool(re.search(r'[A-Z]', password))

    lowercase = bool(re.search(r'[a-z]', password))

    numbers = bool(re.search(r'[0-9]', password))

    specialchar = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    total = length + uppercase + lowercase + numbers + specialchar

    if total == 5:

        return "Strong password"
    
    elif total >= 3:

        return "Good password"
    
    else:

        return "Weak password"

password = input("Enter your password: ")

strength = passwordchecker(password)

print(f"Password strength: {strength}")