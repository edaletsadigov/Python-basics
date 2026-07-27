word = input("Mətni daxil edin: ")
clean = word.lower().replace(" ", "")

if clean == clean[::-1]:
    print(f'"{word}" palindromdur ✓')
else:
    print(f'"{word}" palindrom deyil ✗')



