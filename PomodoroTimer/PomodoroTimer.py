import platform
import subprocess
import sys
import os

def StartPomodoroTimer():
    CorrectTerminal = None
    Confirmation = None
    PomodoroTimerRunning = True
    SmallBreakDuration = None
    LongBreakDuration = None
    LongBreakInterval = None
    PomodorosLength = None
    TotalPomodoros = None
    SeperateTimerWindow = True
    while PomodoroTimerRunning:
        if Confirmation is None:
            Confirmation = input("Do you know how the Pomodoro Technique works? (Y/N): ")
            if Confirmation.lower() == "n" or Confirmation.lower() == "no":
                print('''
The Pomodoro Technique is a time management method that uses a timer to break work into intervals,
traditionally 25 minutes in length, separated by short breaks that are typically 5 minutes long.
Each interval is known as a "pomodoro". After four pomodoros, there is a longer break, typically around 20-30 minutes.
The technique is based on the idea that frequent breaks can improve mental agility and productivity.
''')
                input("Press Enter to continue...")
            elif Confirmation.lower() != "y" and Confirmation.lower() != "yes":
                print("Invalid input. Please enter Y or N.")
                input("Press Enter to continue...")
                Confirmation = None
                continue
        if SmallBreakDuration is None:
            SmallBreakDuration = input("Please enter the duration of the small break in minutes: ")
            try:
                SmallBreakDuration = int(SmallBreakDuration)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                SmallBreakDuration = None
                continue
        if LongBreakDuration is None:
            LongBreakDuration = input("Please enter the duration of the long break in minutes: ")
            try:
                LongBreakDuration = int(LongBreakDuration)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                LongBreakDuration = None
                continue
        if LongBreakInterval is None:
            LongBreakInterval = input("Please enter the interval between long breaks in minutes: ")
            try:
                LongBreakInterval = int(LongBreakInterval)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                LongBreakInterval = None
                continue
        if PomodorosLength is None:
            PomodorosLength = input("Please enter the length of each pomodoro in minutes: ")
            try:
                PomodorosLength = int(PomodorosLength)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                PomodorosLength = None
                continue
        if TotalPomodoros is None:
            TotalPomodoros = input("Please enter the total number of pomodoros you would like to complete: ")
            try:
                TotalPomodoros = int(TotalPomodoros)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                TotalPomodoros = None
                continue
        print(f'''
Please select the operation you would like to perform:

1. Start Pomodoro Timer
2. Change Small Break Duration
3. Change Long Break Duration
4. Change Long Break Interval
5. Change Pomodoro Length
6. Change Total Pomodoros

7. Exit
8. Reset All Settings
9. Toggle Seperate Timer Window (Currently: {SeperateTimerWindow})
10. About the Pomodoro Technique
''')
        Operation = input("Please enter the number for the operation you would like to perform: ")
        try:
            Operation = int(Operation)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            input("Press Enter to continue...")
            Operation = None
        match Operation:
            case 1:
                if SeperateTimerWindow:
                    print("Starting Pomodoro Timer...")
                    if os.path.exists("SeperateTimerWindowsCommunicationFileA.txt"):
                        print("The seperate timer window failed to start properly last time.")
                        input("Press Enter to continue...")
                        os.remove("SeperateTimerWindowsCommunicationFileA.txt")
                    if os.path.exists("SeperateTimerWindowsCommunicationFileB.txt"):
                        print("The seperate timer window was closed before the timer finished.")
                        input("Press Enter to continue...")
                        os.remove("SeperateTimerWindowsCommunicationFileB.txt")
                    with open("SeperateTimerWindowsCommunicationFileA.txt", "w") as f:
                        f.write("THIS FILE IS USED FOR COMMUNICATION BETWEEN THE MAIN POMODORO TIMER AND THE SEPERATE TIMER WINDOW. DO NOT DELETE OR MODIFY THIS FILE.\n")
                    with open("SeperateTimerWindowsCommunicationFileB.txt", "w") as f:
                        f.write("THIS FILE IS USED FOR COMMUNICATION BETWEEN THE MAIN POMODORO TIMER AND THE SEPERATE TIMER WINDOW. DO NOT DELETE OR MODIFY THIS FILE.\n")
                        f.write(f"{SmallBreakDuration}, {LongBreakDuration}, {LongBreakInterval}, {PomodorosLength}, {TotalPomodoros}")
                    if platform.system() == "Windows":
                        subprocess.Popen(["python", "PomodoroTimerWindow.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
                    elif platform.system() == "Linux":
                        if CorrectTerminal:
                            subprocess.Popen([CorrectTerminal, "-e", f"{sys.executable} PomodoroTimerWindow.py"])
                        PotentialTerminals = ["gnome-terminal", "konsole", "xterm", "lxterminal", "xfce4-terminal", "mate-terminal", "terminator"]
                        for terminal in PotentialTerminals:
                            try:
                                print(f"Checking for terminal: {terminal}")
                                subprocess.run([terminal, "-e", "true"], check=True)
                                print("Found terminal:", terminal)
                                CorrectTerminal = terminal
                            except:
                                print("Terminal not found:", terminal)
                        if CorrectTerminal:
                            subprocess.Popen([CorrectTerminal, "-e", f"{sys.executable} PomodoroTimerWindow.py"])
                        else:
                            print("No supported terminal emulator found. Please install one of the following: gnome-terminal, konsole, xterm, lxterminal, xfce4-terminal, mate-terminal, terminator, or disable the seperate timer window option.")
                            input("Press Enter to continue...")
                    elif platform.system() == "Darwin":  # macOS
                        subprocess.Popen(["open", "-a", "Terminal", sys.executable, "PomodoroTimerWindow.py"])
                    else:
                        print("Unsupported operating system. Cannot open a new terminal window. Please disable the seperate timer window option.")
                else:
                    from PomodoroTimerWindow import StartSeperatePomodoroTimerWindow
                    with open("SeperateTimerWindowsCommunicationFileA.txt", "w") as f:  
                        f.write("THIS FILE IS USED FOR COMMUNICATION BETWEEN THE MAIN POMODORO TIMER AND THE SEPERATE TIMER WINDOW. PLEASE DO NOT DELETE OR MODIFY THIS FILE.\n")
                    with open("SeperateTimerWindowsCommunicationFileB.txt", "w") as f:
                        f.write("THIS FILE IS USED FOR COMMUNICATION BETWEEN THE MAIN POMODORO TIMER AND THE SEPERATE TIMER WINDOW. PLEASE DO NOT DELETE OR MODIFY THIS FILE.\n")
                        f.write(f"{SmallBreakDuration}, {LongBreakDuration}, {LongBreakInterval}, {PomodorosLength}, {TotalPomodoros}")
                    StartSeperatePomodoroTimerWindow()
            case 2:
                SmallBreakDuration = None
                continue
            case 3:
                LongBreakDuration = None
                continue
            case 4:
                LongBreakInterval = None
                continue
            case 5:
                PomodorosLength = None
                continue
            case 6:
                TotalPomodoros = None
                continue
            case 7:
                PomodoroTimerRunning = False
                break
            case 8:
                Confirmation = None
                SmallBreakDuration = None
                LongBreakDuration = None
                LongBreakInterval = None
                PomodorosLength = None
                TotalPomodoros = None
                SeperateTimerWindow = True
                continue
            case 9:
                SeperateTimerWindow = not SeperateTimerWindow
                print(f"Seperate Timer Window is now set to: {SeperateTimerWindow}")
                input("Press Enter to continue...")
                continue
            case 10:
                print('''
The Pomodoro Technique is a time management method that uses a timer to break work into intervals,
traditionally 25 minutes in length, separated by short breaks that are typically 5 minutes long.
Each interval is known as a "pomodoro". After four pomodoros, there is a longer break, typically around 20-30 minutes.
The technique is based on the idea that frequent breaks can improve mental agility and productivity.
''')
                input("Press Enter to continue...")
                continue
            case _:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                continue


if __name__ == "__main__":
    StartPomodoroTimer()