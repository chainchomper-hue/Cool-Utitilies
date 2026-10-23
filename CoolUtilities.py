while True:
    print('''
    Which utility would you like to use?

    1. Calculator
    2. Unit Converter
    3. VirtualBox VM Controller
    4. Random Number Generator
    5. Todo List
    6. Exit

    More coming soon!
    ''')

    Utility = input("Please enter the number for the utility you would like to use: ")
    try:
        Utility = int(Utility)
    except ValueError:
        print("Invalid input. Please enter a valid utility number.")
        input("Press Enter to continue...")
        continue

    match Utility:
        case 1:
            from Calculator import StartCalculator
            StartCalculator()
        case 2:
            from UnitConverter import StartUnitConverter
            StartUnitConverter()
        case 3:
            from VirtualBoxVMController import StartVirtualBoxVMController
            StartVirtualBoxVMController()
        case 4:
            from RandomNumberGenerator import StartRandomNumberGenerator
            StartRandomNumberGenerator()
        case 5:
            from TodoList import StartTodoList
            StartTodoList()
        case 6:
            break
        case _:
            print("Invalid input. Please enter a valid utility number.")
            input("Press Enter to continue...")