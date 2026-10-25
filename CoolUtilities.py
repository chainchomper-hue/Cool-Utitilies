
while True:
    print('''
    Which utility would you like to use?

    1. Calculator
    2. Unit Converter
    3. VirtualBox VM Controller
    4. Random Number Generator
    5. Todo List
    6. Pomodoro Timer
    7. Exit

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
            from Calculator.Calculator import StartCalculator
            StartCalculator()
        case 2:
            from UnitConverter.UnitConverter import StartUnitConverter
            StartUnitConverter()
        case 3:
            from VirtualBoxVMController.VirtualBoxVMController import StartVirtualBoxVMController
            StartVirtualBoxVMController()
        case 4:
            from RandomNumberGenerator.RandomNumberGenerator import StartRandomNumberGenerator
            StartRandomNumberGenerator()
        case 5:
            from TodoList.TodoList import StartTodoList
            StartTodoList()
        case 6:
            from PomodoroTimer.PomodoroTimer import StartPomodoroTimer
            StartPomodoroTimer()
        case 7:
            break
        case _:
            print("Invalid input. Please enter a valid utility number.")
            input("Press Enter to continue...")