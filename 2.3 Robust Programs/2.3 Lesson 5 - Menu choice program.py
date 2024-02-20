valid = False
while not valid:
    valid = True
    print("1. Play game")
    print("2. Save game")
    print("3. Quit")
    choice = input("Enter choice:")
    if not choice in ["1","2","3"]:
        valid = False
        
print("Option",choice,"chosen.")

