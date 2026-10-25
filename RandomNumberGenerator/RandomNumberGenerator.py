import random
def StartRandomNumberGenerator():
    RandomNumberGeneratorRunning = True
    JustChanged = False
    Minimum = None
    Maximum = None
    while RandomNumberGeneratorRunning:
        if Minimum is None:
            Minimum = input("Please enter the minimum number: ")
            try:
                Minimum = int(Minimum)
                JustChanged = True
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                Minimum = None
                continue
        if Maximum is None:
            Maximum = input("Please enter the maximum number: ")
            try:
                Maximum = int(Maximum)
                JustChanged = True
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                Maximum = None
                continue
        if Minimum >= Maximum:
            print("The minimum number must be less than the maximum number.")
            input("Press Enter to continue...")
            Minimum = None
            Maximum = None
            continue
        if JustChanged == True:
            RandomNumber = random.randint(Minimum, Maximum)
            JustChanged = False
            print("A random number between", Minimum, "and", Maximum, "is:", RandomNumber)
            input("Press Enter to continue...")
        print('''

Please select the operation you would like to perform:

1. Reroll
2. Change Minimum
3. Change Maximum
4. Exit

''')
        Operation = input("Please enter the number for the operation you would like to perform: ")
        try:
            Operation = int(Operation)
        except ValueError:
            print("Invalid input. Please enter a valid operation number.")
            input("Press Enter to continue...")
            continue
        match Operation:
            case 1:
                RandomNumber = random.randint(Minimum, Maximum)
                print("A random number between", Minimum, "and", Maximum, "is:", RandomNumber)
                input("Press Enter to continue...")
            case 2:
                Minimum = None
            case 3:
                Maximum = None
            case 4:
                RandomNumberGeneratorRunning = False
            case _:
                print("Invalid input. Please enter a valid operation number.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    StartRandomNumberGenerator()