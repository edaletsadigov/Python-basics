parol = input("Parol daxil edin: ")


uzunluq = len(parol)
if uzunluq>=8:
    print("Simvol sayı yetərlidir.")
else:
    print("Simvol sayı yetərli deyil.")

reqem = sum(char.isdigit() for char in parol)
if reqem>=1:
    print("Parolda ən azı bir rəqəm var.")  
else:
    print("Parolda rəqəm yoxdur.")

boyuk = sum("A" <= char <= "Z" for char in parol)
if boyuk>=1:
    print("Parolda ən azı bir böyük hərf var.")
else:
    print("Parolda böyük hərf yoxdur.")

kiçik = sum("a" <= char <= "z" for char in parol)
if kiçik>=1:
    print("Parolda kiçik hərf var.")
else:
    print("Parolda kiçik hərf yoxdur.")

xususi = sum(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in parol)
if xususi>=1:
    print("Parolda xüsusi simvol var.")
else:
    print("Parolda xüsusi simvol yoxdur.")

if uzunluq>=8 and reqem>=1 and boyuk>=1 and xususi>=1:
    print("Parol güclüdür!")
else:
    print("Parol zəifdir.")