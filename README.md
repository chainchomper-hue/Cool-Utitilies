# Cool Utilities Suite

A collection of useful utilites written in python such as a calculator, random number generator, todo list, and more!

## Included utilities

- Main Launcher ( CoolUtilities.py )
  - Allows you to easily launch all the other utilities with only having to run one command or file.

- Calculator ( Calculator.py )
  - Arithmetic calculator with basic math functions to advanced ones such as factorials and square roots.

- Unit Converter ( UnitConverter.py )
  - Can convert between common units of length, capacity, and mass.
  - Supports meters, kilometers, centimeters, millimeters, miles, yards, feet, inches, liters, milliliters, gallons, quarts, pints, cups, fluid ounces, kilograms, grams, milligrams, pounds, and ounces.

- Random Number Generator ( RandomNumberGenerator.py )
  - Generates a random integer between chosen minimum and maximum values.
  - Lets you reroll and adjust ranges easily.

- Todo List ( TodoList.py )
  - Allows you to make todo lists and lets you read, add, remove tasks from them, and also switch between them.
  - Useful for easy to use and light-weight personal task management without needing a large program or dependencies.

- VirtualBox VM Controller ( VirtualBoxVMController.py )
  - Allows you to run, control, and manage VMs through the command line.
  - Intended for people who want a quick way to use VirtualBox without using a large or slow GUI.
  
- Pomodoro Timer ( PomodoroTimer.py )
  - Allows you to run focused work and break sessions with countdowns and timers.

## Project files

- `/CoolUtilities.py` - Main launcher for easily running utilities.
- `/Calculator/Calculator.py` - Calculator.
- `/UnitConverter/UnitConverter.py` - Unit Converter
- `/RandomNumberGenerator/RandomNumberGenerator.py` - Random number generator.
- `/TodoList/TodoList.py` - Todo List management program.
- `/VirtualBoxVMController/VirtualBoxVMController.py` - VirtualBox VM controller.
- `/PomodoroTimer/PomodoroTimer.py` - Pomodoro timer.
  - `/PomodoroTimer/PomodoroTimerWindow.py` - Part of the Pomodoro timer, cannot be ran seperately.

## Getting started

1. Make sure Python 3.10 or later is installed.
2. Open a terminal in this project folder.
3. Run the main launcher:

```bash
python CoolUtilities.py
```

You can also run each individual utility directly: by going into it's folder and running:

```bash
python Calculator.py
python UnitConverter.py
python RandomNumberGenerator.py
python TodoList.py
python VirtualBoxVMController.py
python PomodoroTimer.py
```

## Requirements, compatibility, and notes

- You must use Python 3.10 or later to use all features.
- MacOS functionality has been added but HAS NOT BEEN TESTED due to me not having a Mac.
- All utilities other than the Pomodoro Timer have been tested on Windows but the Pomodoro Timer is yet to be tested due to me switching to Linux, it should still work however.
- The core utilities only use Python's built-in modules only.
- The VirtualBox VM Controller utility requires VirtualBox to be installed and `VBoxManage` to be available on the system.
  - Virtualbox 7.2 is recommended as it is the version the utility was created to work with but different versions may work as long as VBoxManage's syntax and commands are still the same.
  - On Linux, the script uses `/usr/bin/vboxmanage` as the location of VBoxManage by default.
  - On Windows, it checks the default VirtualBox install path.
  - On macOS, it checks the standard application bundle location.
- The seperate timer window on the Pomodoro Timer utility requires the standard Command Prompt / Terminal on Windows and MacOS, however on Linux, it requires one of the below terminal emulators. You can also edit the script to also check for the one you use, also note that the script was only tested on Konsole.
  - gnome-terminal
  - konsole
  - xterm
  - lxterminal
  - xfce4-terminal
  - mate-terminal
  - terminator

## Intended use

These programs are created as a practical, lightweight personal utility suite for everyday usage and tasks. It is simple to use, easy to understand, and easy to modify or add features.

## Future improvements

Some planned ideas may include:

- Expanding unit support.
- Adding VM hardware modification features to the VirtualBox VM controller.
- Improving the todo list with more task-management and possibly encryption features.
- Making the Pomodoro Timer notify of it ending instead of requiring it to be checked.

## AI Usage

- This project is mainly human written however inline suggestions ( VS Code Feature ) were sometimes used but were mostly what I would have written anyway.
- AI was also sometimes used for bug checking, searching how to do things, and a few other tasks, however no fully AI written code was used.
- I also absolutely hate Vibe Coding, however partial AI usage at the level of inline suggestions and finding bugs is perfectly fine to me.
- I understand if you have a much lower bar for what you would call "AI Slop" and this falls under it but personally I don't think it is.

## License

This project is licensed under the MIT License. Please check the file "LICENSE" for more information.
