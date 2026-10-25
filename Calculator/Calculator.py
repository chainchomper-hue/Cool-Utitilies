def StartCalculator():
    CalculatorRunning = True
    Number = None
    input("Note: Due to floating point imprecision, some results may be slightly off. Press Enter to continue...")

    while CalculatorRunning:
        if Number is None:
            Number = input("Please enter your starting number: ")
            try:
                Number = float(Number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                Number = None
                input("Press Enter to continue...")
                continue

        print('''
    Please select the operation you would like to perform:

    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exponent
    6. Sign Change
    7. Root
    8. Factorial
    9. Modulo
    10. Change starting number
    11. Exit
    ''')
        print("Current number is:", Number)

        Operation = input("Please enter the number for the operation you would like to perform: ")

        try:
            Operation = int(Operation)
        except ValueError:
            print("Invalid input. Please enter a valid operation number.")
            input("Press Enter to continue...")
            continue

        match Operation:
    # Add
            case 1:

                Number2 = input("Please enter the number you would like to add: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                Result = Number + Number2
                print("The result of adding", Number, "and", Number2, "is:", Result)
                Number = Result
                input("Press Enter to continue...")
    # Subtract
            case 2:
                Number2 = input("Please enter the number you would like to subtract: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                Result = Number - Number2
                print("The result of subtracting", Number2, "from", Number, "is:", Result)
                Number = Result
                input("Press Enter to continue...")
    # Multiply
            case 3:
                Number2 = input("Please enter the number you would like to multiply by: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                Result = Number * Number2
                print("The result of multiplying", Number, "by", Number2, "is:", Result)
                Number = Result
                input("Press Enter to continue...")
    # Divide
            case 4:
                Number2 = input("Please enter the number you would like to divide by: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                if Number2 == 0:
                    print("Haha, very funny. You can't divide by zero. Please try again.")
                else:
                    Result = Number / Number2
                    print("The result of dividing", Number, "by", Number2, "is:", Result)
                    Number = Result
                    input("Press Enter to continue...")
    # Exponentiate
            case 5:
                Number2 = input("Please enter the exponent you would like to raise the number to: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                Result = Number ** Number2
                print("The result of raising", Number, "to the power of", Number2, "is:", Result)
                Number = Result
                input("Press Enter to continue...")
    # Change Sign
            case 6:
                Result = -Number
                print("The result of changing the sign of", Number, "is:", Result)
                Number = Result
                input("Press Enter to continue...") 
    # Take Root
            case 7:
                Number2 = input("Please enter the root you would like to take: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                if Number2 == 0:
                    print("Haha, very funny. You can't take the zeroth root. Please try again.")
                elif Number < 0:
                    print("Haha, very funny. You can't take the root of a negative number. Please try again.")
                else:
                    Result = Number ** (1 / Number2)
                    print("The result of taking the", Number2, "root of", Number, "is:", Result)
                    Number = Result
                    input("Press Enter to continue...")
    # Take Factorial
            case 8:
                Number = input("Please enter the number you would like to take the factorial of: ")
                try:
                    Number = float(Number)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                if Number < 0:
                    print("Haha, very funny. You can't take the factorial of a negative number. Please try again.")
                elif Number.is_integer() == False:
                    print("Haha, very funny. You can't take the factorial of a non-integer number. Please try again.")
                else:
                    Number = int(Number)
                    Result = 1
                    for i in range(1, Number + 1):
                        Result *= i
                    print("The result of taking the factorial of", Number, "is:", Result)
                    Number = Result
                    input("Press Enter to continue...")
    # Modulo
            case 9:
                Number2 = input("Please enter the number you would like to take the modulo of: ")
                try:
                    Number2 = float(Number2)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    input("Press Enter to continue...")
                    continue
                if Number2 == 0:
                    print("Haha, very funny. You can't take the modulo by zero. Please try again.")
                else:
                    Result = Number % Number2
                    print("The result of taking", Number, "modulo", Number2, "is:", Result)
                    Number = Result
                    input("Press Enter to continue...")
    # Change Starting Number
            case 10:
                Number = None
    # Exit
            case 11:
                CalculatorRunning = False
    # Invalid Operation
            case _:
                print("Invalid operation. Please try again.")

if __name__ == "__main__":
    StartCalculator()