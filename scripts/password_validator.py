password = input("Enter a password: ")

length = len(password)
if length >= 8:
    print("Password length is sufficient.")
else:
    print("Password is too short.")

digit = sum(char.isdigit() for char in password)
if digit >= 1:
    print("Password contains at least one digit.")
else:
    print("Password has no digits.")

uppercase = sum(char.isupper() for char in password)
if uppercase >= 1:
    print("Password contains at least one uppercase letter.")
else:
    print("Password has no uppercase letters.")

lowercase = sum(char.islower() for char in password)
if lowercase >= 1:
    print("Password contains at least one lowercase letter.")
else:
    print("Password has no lowercase letters.")

special = sum(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)
if special >= 1:
    print("Password contains at least one special character.")
else:
    print("Password has no special characters.")

if length >= 8 and digit >= 1 and uppercase >= 1 and special >= 1:
    print("Strong password!")
else:
    print("Weak password.")
