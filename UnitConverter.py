UnitConverterRunning = False
print("Due to floating point imprecision, some results may be slightly off. Press Enter to continue...")
input("Press Enter to continue...")
def StartUnitConverter():
    UnitConverterRunning = True
    while UnitConverterRunning:
        print('''

Please select the unit you would like to convert from:

Length Units:
    1. Meters
    2. Kilometers
    3. Centimeters
    4. Millimeters
    5. Miles
    6. Yards
    7. Feet
    8. Inches

Capacity Units:
    9. Liters
    10. Milliliters
    11. Gallons
    12. Quarts
    13. Pints
    14. Cups
    15. Fluid Ounces

Mass Units:
    16. Kilograms
    17. Grams
    18. Milligrams
    19. Pounds
    20. Ounces

Controls:
    0. Exit
''')
        UnitA = input("Please select the number corresponding to the starting unit you would like to convert from: ")
        try:
            UnitA = int(UnitA)
        except ValueError:
            print("Invalid input. Please enter a valid unit number.")
            input("Press Enter to continue...")
            continue

        if UnitA == 0:
            UnitConverterRunning = False
            break

        if UnitA < 0 or UnitA > 20:
            print("Invalid unit selection. Please try again.")
            input("Press Enter to continue...")
            continue

        UnitAAmount = input("Please enter the amount of the starting unit you would like to convert: ")
        try:
            UnitAAmount = float(UnitAAmount)    
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            input("Press Enter to continue...")
            continue

        match UnitA:
            # Length Units
            case _ if UnitA > 0 and UnitA < 9:
                print('''

Please select a unit of the same type to convert to:

1. Meters
2. Kilometers
3. Centimeters
4. Millimeters
5. Miles
6. Yards
7. Feet
8. Inches
''')
                UnitB = input("Please select the number corresponding to the unit you would like to convert to: ")
                try:
                    UnitB = int(UnitB)
                except ValueError:
                    print("Invalid input. Please enter a valid unit number.")
                    input("Press Enter to continue...")
                    continue
                # Convert to meters first for less complexity.
                match UnitA:
                    case 1:  # Meters
                        amount_in_meters = UnitAAmount
                    case 2:  # Kilometers
                        amount_in_meters = UnitAAmount * 1000
                    case 3:  # Centimeters
                        amount_in_meters = UnitAAmount / 100
                    case 4:  # Millimeters
                        amount_in_meters = UnitAAmount / 1000
                    case 5:  # Miles
                        amount_in_meters = UnitAAmount * 1609.34
                    case 6:  # Yards
                        amount_in_meters = UnitAAmount * 0.9144
                    case 7:  # Feet
                        amount_in_meters = UnitAAmount * 0.3048
                    case 8:  # Inches
                        amount_in_meters = UnitAAmount * 0.0254
                    case _:
                        print("Invalid unit selection. Please try again.")
                        input("Press Enter to continue...")
                        continue
                # Now convert from meters to the desired unit.
                match UnitB:
                    case 1:  # Meters
                        converted_amount = amount_in_meters
                    case 2:  # Kilometers
                        converted_amount = amount_in_meters / 1000
                    case 3:  # Centimeters
                        converted_amount = amount_in_meters * 100
                    case 4:  # Millimeters
                        converted_amount = amount_in_meters * 1000
                    case 5:  # Miles
                        converted_amount = amount_in_meters / 1609.34
                    case 6:  # Yards
                        converted_amount = amount_in_meters / 0.9144
                    case 7:  # Feet
                        converted_amount = amount_in_meters / 0.3048
                    case 8:  # Inches
                        converted_amount = amount_in_meters / 0.0254
                    case _:
                        print("Invalid unit selection. Please try again.")
                        input("Press Enter to continue...")
                        continue
                print(f"{UnitAAmount} of unit {UnitA} is equal to {converted_amount} of unit {UnitB}.")
                input("Press Enter to continue...")
            # Capacity Units
            case _ if UnitA > 8 and UnitA < 16:
                print('''

Please select a unit of the same type to convert to:

9. Liters
10. Milliliters
11. Gallons
12. Quarts
13. Pints
14. Cups
15. Fluid Ounces
                ''')
                UnitB = input("Please select the number corresponding to the unit you would like to convert to: ")
                try:
                    UnitB = int(UnitB)
                except ValueError:
                    print("Invalid input. Please enter a valid unit number.")
                    input("Press Enter to continue...")
                    continue
                # Convert to liters first for less complexity.
                match UnitA:
                    case 9:  # Liters
                        amount_in_liters = UnitAAmount
                    case 10:  # Milliliters
                        amount_in_liters = UnitAAmount / 1000
                    case 11:  # Gallons
                        amount_in_liters = UnitAAmount * 3.78541
                    case 12:  # Quarts
                        amount_in_liters = UnitAAmount * 0.946353
                    case 13:  # Pints
                        amount_in_liters = UnitAAmount * 0.473176
                    case 14:  # Cups
                        amount_in_liters = UnitAAmount * 0.24
                    case 15:  # Fluid Ounces
                        amount_in_liters = UnitAAmount * 0.0295735
                    case _:
                        print("Invalid unit selection. Please try again.")
                        input("Press Enter to continue...")
                        continue
                # Now convert from liters to the desired unit.
                match UnitB:
                    case 9:  # Liters
                        converted_amount = amount_in_liters
                    case 10:  # Milliliters
                        converted_amount = amount_in_liters * 1000
                    case 11:  # Gallons
                        converted_amount = amount_in_liters / 3.78541
                    case 12:  # Quarts
                        converted_amount = amount_in_liters / 0.946353
                    case 13:  # Pints
                        converted_amount = amount_in_liters / 0.473176
                    case 14:  # Cups
                        converted_amount = amount_in_liters / 0.24
                    case 15:  # Fluid Ounces
                        converted_amount = amount_in_liters / 0.0295735
                    case _:
                        print("Invalid unit selection. Please try again.")
                        input("Press Enter to continue...")
                        continue
                print(f"{UnitAAmount} of unit {UnitA} is equal to {converted_amount} of unit {UnitB}.")
                input("Press Enter to continue...")
            # Mass Units
            case _ if UnitA > 15 and UnitA < 21:
                print('''
                
Please select a unit of the same type to convert to:
                
16. Kilograms
17. Grams
18. Milligrams
19. Pounds
20. Ounces
                ''')
                UnitB = input("Please select the number corresponding to the unit you would like to convert to: ")
                try:
                    UnitB = int(UnitB)
                except ValueError:
                    print("Invalid input. Please enter a valid unit number.")
                    input("Press Enter to continue...")
                    continue
                # Convert to kilograms first for less complexity.
                match UnitA:
                    case 16:  # Kilograms
                        amount_in_kilograms = UnitAAmount
                    case 17:  # Grams
                        amount_in_kilograms = UnitAAmount / 1000
                    case 18:  # Milligrams
                        amount_in_kilograms = UnitAAmount / 1e6
                    case 19:  # Pounds
                        amount_in_kilograms = UnitAAmount * 0.453592
                    case 20:  # Ounces
                        amount_in_kilograms = UnitAAmount * 0.0283495
                    case _:
                        print("Invalid unit selection. Please try again.")
                        input("Press Enter to continue...")
                        continue
                # Now convert from kilograms to the desired unit.
                match UnitB:
                    case 16:  # Kilograms
                        converted_amount = amount_in_kilograms
                    case 17:  # Grams
                        converted_amount = amount_in_kilograms * 1000
                    case 18:  # Milligrams
                        converted_amount = amount_in_kilograms * 1e6
                    case 19:  # Pounds
                        converted_amount = amount_in_kilograms / 0.453592
                    case 20:  # Ounces
                        converted_amount = amount_in_kilograms / 0.0283495
                    case _:
                        print("Invalid unit selection. Please try again.") 
                        input("Press Enter to continue...")
                        continue
                print(f"{UnitAAmount} of unit {UnitA} is equal to {converted_amount} of unit {UnitB}.")
                input("Press Enter to continue...")
            # Invalid Selection
            case _:
                print("Invalid unit selection. Please try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    StartUnitConverter()
