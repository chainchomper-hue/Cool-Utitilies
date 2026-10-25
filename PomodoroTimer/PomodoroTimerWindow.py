import os
import subprocess
import time

PomodorosCompleted = 0

def ClearScreen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def Timer(Time, Message):
    TimerRunning = True
    Timer = 0
    while TimerRunning:
        ClearScreen()
        Timer += 1
        print(f"Time remaining: {Time * 60 - Timer} seconds")
        print(Message)
        time.sleep(1)
        if Timer >= Time * 60:
            TimerRunning = False

def StartSeperatePomodoroTimerWindow():
    if os.path.exists("SeperateTimerWindowsCommunicationFileA.txt"):
        os.remove("SeperateTimerWindowsCommunicationFileA.txt")
        with open("SeperateTimerWindowsCommunicationFileB.txt", "r") as f:
            Lines = f.readlines()
        Lines = Lines[1].split(", ")
        if len(Lines) >= 5:
            SmallBreakDuration = int(Lines[0])
            LongBreakDuration = int(Lines[1])
            LongBreakInterval = int(Lines[2])
            PomodorosLength = int(Lines[3])
            TotalPomodoros = int(Lines[4])
        print(f"{SmallBreakDuration=}, {LongBreakDuration=}, {LongBreakInterval=}, {PomodorosLength=}, {TotalPomodoros=}")
        MainTimerRunning = True
        while MainTimerRunning:
            input(f"Press Enter to start a Pomodoro of {PomodorosLength} minute/s...")
            Timer(PomodorosLength, f"Currently working for {PomodorosLength} minute/s...")
            print("Pomodoro completed!")
            PomodorosCompleted += 1
            print(f"Pomodoros completed: {PomodorosCompleted}/{TotalPomodoros}")
            if PomodorosCompleted >= TotalPomodoros:
                print("All Pomodoros completed! Great job!")
                input("Press Enter to continue...")
                os.remove("SeperateTimerWindowsCommunicationFileB.txt")
                MainTimerRunning = False
            elif PomodorosCompleted % LongBreakInterval == 0:
                print("Time for a long break!")
                input(f"Press Enter to start a long break of {LongBreakDuration} minute/s...")
                Timer(LongBreakDuration, f"Taking a long break of {LongBreakDuration} minute/s...")
            else:
                print("Time for a short break!")
                input(f"Press Enter to start a short break of {SmallBreakDuration} minute/s...")
                Timer(SmallBreakDuration, f"Taking a short break of {SmallBreakDuration} minute/s...")

    else:
        print("This program does not appear to have been run from the main Pomodoro Timer program. This is not a standalone program, please run PomodoroTimer.py instead.")

if __name__ == "__main__":
    StartSeperatePomodoroTimerWindow()