import subprocess
import platform
import re
import os
import sys
CustomVboxManagePath = None

if CustomVboxManagePath is not None:
    VboxManagePath = CustomVboxManagePath
elif platform.system() == "Windows":
    VboxManagePath = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
elif platform.system() == "Linux":
    VboxManagePath = r"/usr/bin/vboxmanage"
elif platform.system() == "Darwin":
    VboxManagePath = r"/Applications/VirtualBox.app/Contents/MacOS/VBoxManage"
else:
    print("Unknown operating system. Please set the CustomVboxManagePath variable to the path of VBoxManage on your system.")
    input("Press Enter to continue...")
    sys.exit(1)

if not os.path.isfile(VboxManagePath):
    print(f"VBoxManage not found at {VboxManagePath}. Please ensure VirtualBox is installed or the CustomVboxManagePath variable is set to the correct path.")
    input("Press Enter to continue...")
    sys.exit(1)
    
State = None

KEY_MAP = {
    "a": ("1e", "9e"),                  # A
    "b": ("30", "b0"),                  # B
    "c": ("2e", "ae"),                  # C
    "d": ("20", "a0"),                  # D
    "e": ("12", "92"),                  # E
    "f": ("21", "a1"),                  # F
    "g": ("22", "a2"),                  # G
    "h": ("23", "a3"),                  # H
    "i": ("17", "97"),                  # I
    "j": ("24", "a4"),                  # J
    "k": ("25", "a5"),                  # K
    "l": ("26", "a6"),                  # L
    "m": ("32", "b2"),                  # M
    "n": ("31", "b1"),                  # N
    "o": ("18", "98"),                  # O
    "p": ("19", "99"),                  # P
    "q": ("10", "90"),                  # Q
    "r": ("13", "93"),                  # R
    "s": ("1f", "9f"),                  # S
    "t": ("14", "94"),                  # T
    "u": ("16", "96"),                  # U
    "v": ("2f", "af"),                  # V
    "w": ("11", "91"),                  # W
    "x": ("2d", "ad"),                  # X
    "y": ("15", "95"),                  # Y
    "z": ("2c", "ac"),                  # Z
    "1": ("02", "82"),                  # 1
    "2": ("03", "83"),                  # 2
    "3": ("04", "84"),                  # 3
    "4": ("05", "85"),                  # 4
    "5": ("06", "86"),                  # 5
    "6": ("07", "87"),                  # 6
    "7": ("08", "88"),                  # 7
    "8": ("09", "89"),                  # 8
    "9": ("0a", "8a"),                  # 9
    "0": ("0b", "8b"),                  # 0
    ",": ("33", "b3"),                  # Comma
    ".": ("34", "b4"),                  # Period
    "/": ("35", "b5"),                  # Forward Slash
    ";": ("27", "a7"),                  # Semicolon
    "'": ("28", "a8"),                  # Apostrophe
    "[": ("1a", "9a"),                  # Left Bracket
    "]": ("1b", "9b"),                  # Right Bracket
    "\\": ("2b", "ab"),                  # Backslash
    "-": ("0c", "8c"),                  # Minus
    "=": ("0d", "8d"),                  # Equals
    "`": ("29", "a9"),                  # Backtick
    "!": ("2a", "02", "82", "aa"),      # Exclamation Mark
    "@": ("2a", "03", "83", "aa"),      # At Sign
    "#": ("2a", "04", "84", "aa"),      # Hash
    "$": ("2a", "05", "85", "aa"),      # Dollar Sign
    "%": ("2a", "06", "86", "aa"),      # Percent Sign
    "^": ("2a", "07", "87", "aa"),      # Caret
    "&": ("2a", "08", "88", "aa"),      # Ampersand
    "*": ("2a", "09", "89", "aa"),      # Asterisk
    "(": ("2a", "0a", "8a", "aa"),      # Left Parenthesis
    ")": ("2a", "0b", "8b", "aa"),      # Right Parenthesis
    "_": ("2a", "0c", "8c", "aa"),      # Underscore
    "+": ("2a", "0d", "8d", "aa"),      # Plus
    "{": ("2a", "1a", "9a", "aa"),      # Left Brace
    "}": ("2a", "1b", "9b", "aa"),      # Right Brace
    "|": ("2a", "2b", "ab", "aa"),      # Vertical Bar
    ":": ("2a", "27", "a7", "aa"),      # Colon
    '"': ("2a", "28", "a8", "aa"),      # Quotation Mark
    "~": ("2a", "29", "a9", "aa"),      # Tilde
    "<": ("2a", "33", "b3", "aa"),      # Less Than
    ">": ("2a", "34", "b4", "aa"),      # Greater Than
    "?": ("2a", "35", "b5", "aa"),      # Question Mark
    "escape": ("01", "81"),
    "delete": ("e0", "53", "e0", "d3"),
    "insert": ("e0", "52", "e0", "d2"),
    "home": ("e0", "47", "e0", "c7"),
    "end": ("e0", "4f", "e0", "cf"),
    "tab": ("0f", "8f"),
    "caps lock": ("3a", "ba"),
    "shift": ("2a", "aa"),
    "control": ("1d", "9d"),
    "super/windows": ("e0", "5b", "e0", "db"),
    "alt": ("38", "b8"),
    "enter": ("1c", "9c"),
    "backspace": ("0e", "8e"),
    "space": ("39", "b9"),
    "up arrow": ("e0", "48", "e0", "c8"),
    "down arrow": ("e0", "50", "e0", "d0"),
    "left arrow": ("e0", "4b", "e0", "cb"),
    "right arrow": ("e0", "4d", "e0", "cd"),

    # Aliases

    "esc": ("01", "81"),
    "del": ("e0", "53", "e0", "d3"),
    "ins": ("e0", "52", "e0", "d2"),
    "ctrl": ("1d", "9d"),
    "win": ("e0", "5b", "e0", "db"),
    "windows": ("e0", "5b", "e0", "db"),
    "super": ("e0", "5b", "e0", "db"),
}

def VMCreator():
    VMCreatorRunning = True
    OSList = []
    while VMCreatorRunning:
        VMName = input("Please enter the name of the new VM or 'quit' to stop VM creation: ")
        if VMName.lower() == "quit":
            print("VM creation cancelled.")
            input("Press Enter to continue...")
            VMCreatorRunning = False
            continue
        if not VMName:
            print("VM name cannot be empty. Please enter a valid name.")
            input("Press Enter to continue...")
            continue
        try:
            OSList = subprocess.run([VboxManagePath, "list", "ostypes"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            OSList = OSList.stdout.decode("utf-8")
            OSList = re.findall(
                r"^ID / Description:\s*(\S+)",
                OSList,
                re.MULTILINE
            )
            if not OSList:
                print("There were no supported OS types found, this shouldn't even be possible. Make sure VirtualBox is not corrupt or a different version than 7.2.12.")
                input("Press Enter to continue...")
                VMCreatorRunning = False
                continue
            OSList.append("Cancel")
            print("Supported OS types:")
            for i, os_type in enumerate(OSList, 1):
                print(f"{i}. {os_type}")
            OSSelection = input("Please select the number corresponding to the OS type for the new VM: ")
            try:
                OSSelection = int(OSSelection)
                if OSSelection < 1 or OSSelection > len(OSList):
                    raise ValueError
                OSID = OSList[OSSelection - 1]
            except ValueError:
                print("Invalid selection. Please enter a valid number corresponding to the OS type.")
                input("Press Enter to continue...")
                continue
            if OSID.lower() == "cancel":
                print("VM creation cancelled.")
                input("Press Enter to continue...")
                VMCreatorRunning = False
                continue
            print(f"You are about to create a new VM with the following details:\nName: {VMName}\nOS Type: {OSID}.\nIs this correct? (y/n)")
            Confirmation = input().lower()
            if Confirmation in ["y", "yes"]:
                subprocess.run([VboxManagePath, "createvm", "--name", VMName, "--ostype", OSID, "--register"], check=True, stderr=subprocess.PIPE)
                print(f"VM '{VMName}' with OS type '{OSID}' has been created successfully.")
                print("Please note that there is no feature to modify VM hardware yet. Right now VMs are created with the default minimal hardware, please use the VirtualBox GUI to modify VMs.")
                input("Press Enter to continue...")
                VMCreatorRunning = False
                break
            elif Confirmation in ["n", "no"]:
                print("VM creation cancelled.")
                input("Press Enter to continue...")
                VMCreatorRunning = False
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                input("Press Enter to continue...")
        except subprocess.CalledProcessError as e:
            print(e.stderr.decode("utf-8"))
            print("Error occurred while creating VM, check above for details:")
            input("Press Enter to continue...")
            VMCreatorRunning = False

def ComboMaker():
    Combo = []
    ComboMakerRunning = True
    while ComboMakerRunning:
        print('''

Please create the special key combo you would like to press.

1. Toggle a special key (Shift, Control, Alt, etc.)
2. Toggle a normal key (A, B, C, 1, 2, 3, etc.)
3. Press the combo
4. Exit

''')
        print("Current combo is:", Combo)
        Operation = input("Please enter the number for the operation you would like to perform: ")
        try:
            Operation = int(Operation)
        except ValueError:
            print("Invalid input. Please enter a valid operation number.")
            input("Press Enter to continue...")
            continue
        match Operation:
            case 1:
                # Toggle a special key (Shift, Control, Alt, etc.)
                print('''
Please type the name of the special key you would like to toggle.

Keys:
    Escape
    Delete
    Insert
    Home
    End
    Tab
    Caps Lock
    Shift
    Control
    Super/Windows
    Alt
    Enter
    Backspace
    Space
    Up Arrow
    Down Arrow
    Left Arrow
    Right Arrow

    Cancel
    ''')
                Key = input("Please enter the name of the key you want to toggle: ").strip().lower()
                if Key == "cancel":
                    continue
                if Key in KEY_MAP:
                    if Key.lower() in Combo:
                        Combo.remove(Key.lower())
                    else:
                        Combo.append(Key.lower())
                else:
                    print("Invalid option selected.")
                    input("Press Enter to continue...")
                    continue
            case 2:
                # Toggle a normal key (A, B, C, 1, 2, 3, etc.)
                Key = input("Please enter the letter or symbol you would like to add to the combo: ")
                if Key.lower() in KEY_MAP:
                    if Key.lower() in Combo:
                        Combo.remove(Key.lower())
                    else:
                        Combo.append(Key.lower())
                else:
                    print("Invalid letter or symbol. Please enter a valid letter or symbol or make sure you didn't type multiple letters or symbols at once.")
                    input("Press Enter to continue...")
                    continue
            case 3:
                PressScanCodes = []
                ReleaseScanCodes = []
                CombinedScanCodes = []
                if not Combo:
                    print("No keys in the combo. Please add keys to the combo before pressing it.")
                    input("Press Enter to continue...")
                    continue
                for key in Combo:
                    if key in KEY_MAP:
                        press_codes = KEY_MAP[key][:len(KEY_MAP[key]) // 2]
                        release_codes = KEY_MAP[key][len(KEY_MAP[key]) // 2:]
                        PressScanCodes.extend(press_codes)
                        ReleaseScanCodes.extend(release_codes)
                CombinedScanCodes = PressScanCodes + ReleaseScanCodes
                try:
                    cmd = [VboxManagePath, "controlvm", CurrentVM, "keyboardputscancode"] + CombinedScanCodes
                    subprocess.run(cmd, check=True, stderr=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    print(e.stderr.decode("utf-8"))
                    print("Error occurred while sending the selected key combo, check above for details.")
                    input("Press Enter to continue...")
                    continue
                print(f"Sent Combo: {Combo}")
                input("Press Enter to continue...")
            case 4:
                PressScanCodes = []
                ReleaseScanCodes = []
                CombinedScanCodes = []
                Combo = []
                ComboMakerRunning = False

def CheckForVMs():
    global VirtualBoxVMControllerRunning
    global CurrentVM
    VMList = []
    try:
        VBoxManageList = subprocess.run([VboxManagePath, "list", "vms"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode("utf-8"))
        print("Error occurred while running VBoxManage, check above for details:")
        input("Press Enter to continue...")
        VirtualBoxVMControllerRunning = False
        return
    except FileNotFoundError:
        print("VBoxManage not found. Please ensure VirtualBox is installed or the CustomVboxManagePath variable is set to the correct path.")
        input("Press Enter to continue...")
        VirtualBoxVMControllerRunning = False
        return
    VBoxManageList = VBoxManageList.stdout.decode("utf-8").strip()
    VBoxManageList = re.findall(r'"([^"]+)"', VBoxManageList)
    for item in VBoxManageList:
        if item != "<inaccessible>":
            VMList.append(item)
    if not VMList:
        print("No accessible VMs found, please create a new VM or make sure that your VMs are stored on an accessible disk.")
        input("Press enter to continue...")
    VMList.insert(0, "Exit")
    VMList.insert(1, "Create a new VM")
    print("Available VMs:")
    for i, item in enumerate(VMList, 0):
        print(f"{i}. {item}")
    VMSelection = input("Please select the number corresponding to the VM you would like to control: ")
    try:
        VMSelection = int(VMSelection)
        if VMSelection < 0:
            print("Please enter a valid VM number.")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("Invalid Value, please type in a valid VM selection.")
        input("Press enter to continue...")
        return

    try:
        CurrentVM = VMList[VMSelection]
    except IndexError:
        print("Please enter a valid VM number.")
        input("Press enter to continue...")

def GetVMState():
    global VirtualBoxVMControllerRunning
    global State
    State = "unknown"
    try:
        VMInfo = subprocess.run(
            [VboxManagePath, "showvminfo", CurrentVM],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        VMInfo = VMInfo.stdout.strip()
        if not VMInfo:
            raise RuntimeError("No VM info returned from VBoxManage.")

        for line in VMInfo.splitlines():
            if line.lower().startswith("state:"):
                raw_state = line.split(":", 1)[1].strip().lower()
                if not raw_state:
                    State = "unknown"
                else:
                    State = raw_state.split()[0]
                    if State == "powered":
                        State = "powered off"
                break
        else:
            State = "unknown"
    except Exception:
        print("Failed to get VM state.")
        input("Press enter to continue... ")
        VirtualBoxVMControllerRunning = False


def StartVirtualBoxVMController():
    global CurrentVM
    global State
    global VirtualBoxVMControllerRunning
    print("This utility requires VirtualBox to be installled on your system. If you do not have VirtualBox installed, please install it before using this utility.")
    input("Press Enter to continue...")
    CurrentVM = None
    VirtualBoxVMControllerRunning = False
    try:
        Version = subprocess.run([VboxManagePath, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        Version = Version.stdout.decode("utf-8").strip()
        print(f"VboxManage Detected with Version: {Version}")
        if not(Version.startswith("7.2")):
            print("Warning: This script was designed for VirtualBox 7.2, if you are using an different release some features may not work correctly. For best compatibility, it is recommended to use VirtualBox 7.2 as this was the current version when the script was made. I wont stop you but be wary of potential issues.")
            input("Press Enter to continue...")
        VirtualBoxVMControllerRunning = True
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode("utf-8"))
        print("Error occurred while running VBoxManage, check above for details:")
        input("Press Enter to continue...")
    except FileNotFoundError:
        print("VBoxManage not found. Please ensure VirtualBox is installed or the CustomVboxManagePath variable is set to the correct path.")
        input("Press Enter to continue...")
    while VirtualBoxVMControllerRunning:
        if CurrentVM is None:
            CheckForVMs()
            if CurrentVM == "Exit":
                VirtualBoxVMControllerRunning = False
                break
            if CurrentVM == "Create a new VM":
                VMCreator()
                CurrentVM = None
                continue
            if CurrentVM == None:
                continue
            GetVMState()
        print('''

Please select the operation you would like to perform:

VM Management:
    1. List all VMs
    2. Create a new VM
    3. Start the VM
    4. Stop the VM
    5. Pause the VM
    6. Resume the VM
    7. Reset the VM
    8. Restore the VM to the latest snapshot
    9. Create a snapshot of the VM

Control running VMs:
    10. Send text input to the VM
    11. Send special key presses to the VM ( Enter, Escape, Delete, etc. )
    12. Send special key combo to the VM
    13. Take and open a screenshot of the VM

Controls:
    0. Exit
    -1. Different VM
''')
        print(f"Currently controlling {CurrentVM}")
        print(f'VM State is currently "{State}".')
        Operation = input("Please enter the number for the operation you would like to perform: ")
        try:
            Operation = int(Operation)
        except ValueError:
            print("Invalid input. Please enter a valid operation number.")
            input("Press Enter to continue...")
            continue
        match Operation:
            # Different VM.
            case -1:
                CurrentVM = None
            # Exit.
            case 0:
                VirtualBoxVMControllerRunning = False
                break
            # List all VMs.
            case 1:
                try:
                    subprocess.run([VboxManagePath, "list", "vms"], check=True, stderr=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    print(e.stderr.decode("utf-8"))
                    print("Error occurred while listing VMs, check above for details:")
                    input("Press Enter to continue...")
                    continue 
                input("Press Enter to continue...")
                continue
            # Create a new VM.
            case 2:
                VMCreator()
            # Start the VM.
            case 3:
                if State in {"running", "paused"}:
                    print("VM is already running.")
                    input("Press Enter to continue...")
                    continue
                try:
                    subprocess.run([VboxManagePath, "startvm", CurrentVM], check=True, stderr=subprocess.PIPE)
                    GetVMState()
                except subprocess.CalledProcessError as e:
                    print(e.stderr.decode("utf-8"))
                    print("Error occurred while starting the VM, check above for details:")
                    input("Press Enter to continue...")
                    continue
            # Stop the VM.
            case 4:
                if State in {"running", "paused"}:
                    try:
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "poweroff"], check=True, stderr=subprocess.PIPE)
                        GetVMState()
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while powering off the VM, check above for details:")
                        input("Press Enter to continue...")
                        continue
                else:
                    print("VM is already powered off.")
                    input("Press Enter to continue...")
            # Pause the VM.
            case 5:
                if State == "running":
                    try:
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "pause"], check=True, stderr=subprocess.PIPE)
                        GetVMState()
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while pausing the VM, check above for details:")
                        input("Press Enter to continue...")
                        continue
                else:
                    print("VM is not running or already paused.")
                    input("Press Enter to continue...")
            # Resume the VM.
            case 6:
                if State == "paused":
                    try:
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "resume"], check=True, stderr=subprocess.PIPE)
                        GetVMState()
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while resuming the VM, check above for details:")
                        input("Press Enter to continue...")
                        continue
                else:
                    print("VM is not paused.")
            # Reset the VM.
            case 7:
                if State == "running":
                    try:
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "reset"], check=True, stderr=subprocess.PIPE)
                        GetVMState()
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while resetting the VM, check above for details:")
                        input("Press Enter to continue...")
                        continue
                else:
                    print("VM is not running.")
                    input("Press Enter to continue...")
            # Restore the VM to the latest snapshot.
            case 8:
                if State in {"running", "paused"}:
                    try:
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "poweroff"], check=True, stderr=subprocess.PIPE)
                        GetVMState()
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while powering off the VM, check above for details:")
                        input("Press Enter to continue...")
                        continue
                try:
                    subprocess.run([VboxManagePath, "snapshot", CurrentVM, "restorecurrent"], check=True, stderr=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    print(e.stderr.decode("utf-8"))
                    print("Error occurred while restoring the VM to the latest snapshot, check above for details:")
                    input("Press Enter to continue...")
                    continue
                try:
                    subprocess.run([VboxManagePath, "startvm", CurrentVM], check=True)
                    GetVMState()
                except subprocess.CalledProcessError as e:
                    print(e.stderr.decode("utf-8"))
                    print("Error occurred while starting the VM, check above for details:")
                    input("Press Enter to continue...")
                    continue
            # Create a snapshot of the VM.
            case 9:
                try:
                    SnapshotName = input("Please enter a name for the snapshot: ")
                    if not SnapshotName:
                        print("Snapshot name cannot be empty. Please enter a valid name.")
                        input("Press Enter to continue...")
                        continue
                    subprocess.run([VboxManagePath, "snapshot", CurrentVM, "take", SnapshotName], check=True, stderr=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    print(e.stderr.decode("utf-8"))
                    print("Error occurred while taking a snapshot of the VM, check above for details:")
                    input("Press Enter to continue...")
                    continue
            # Send text input to the VM.
            case 10:
                if State == "running":
                    Text = input("Please type the text you want to send to the VM: ")
                    try:
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "keyboardputstring", Text], check=True, stderr=subprocess.PIPE)
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while sending text to the VM, check above for details:")
                        input("Press Enter to continue...")
                        continue
                    EnterAfterText = input("Do you want to press Enter? (y/n): ").strip().lower()
                    if EnterAfterText in ["y", "yes"]:
                        try:
                            subprocess.run([VboxManagePath, "controlvm", CurrentVM, "keyboardputscancode", "1c", "9c"], check=True, stderr=subprocess.PIPE)
                        except subprocess.CalledProcessError as e:
                            print(e.stderr.decode("utf-8"))
                            print("Error occurred while sending Enter to the VM, check above for details:")
                            input("Press Enter to continue...")
                            continue
                    elif EnterAfterText not in ["n", "no"]:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                        input("Press Enter to continue...")
                else:
                    print("VM is not running.")
                    input("Press Enter to continue...")
            # Send special key presses to the VM.
            case 11:
                if State == "running":
                    print('''
Please type the name of the special key you would like to press.

Keys:
    Escape
    Delete
    Insert
    Home
    End
    Tab
    Caps Lock
    Shift
    Control
    Super/Windows
    Alt
    Enter
    Backspace
    Space
    Up Arrow
    Down Arrow
    Left Arrow
    Right Arrow

    Cancel
    ''')
                    Key = input("Please enter the name of the key you want to press: ").strip().lower()
                    if Key == "cancel":
                        continue
                    if Key in KEY_MAP:
                        try:
                            cmd = [VboxManagePath, "controlvm", CurrentVM, "keyboardputscancode"] + list(KEY_MAP[Key.lower()])
                            subprocess.run(cmd, check=True, stderr=subprocess.PIPE)
                        except subprocess.CalledProcessError as e:
                            print(e.stderr.decode("utf-8") if e.stderr else e)
                            print("Error occurred while sending the selected key, check above for details.")
                            input("Press Enter to continue...")
                            continue
                    else:
                        print("Invalid option selected.")
                        input("Press Enter to continue...")
                        continue
                else:
                    print("VM is not running.")
                    input("Press enter to continue...")
            # Send special key combo to the VM.
            case 12:
                if State == "running":
                    ComboMaker()
                else:
                    print("VM is not running.")
                    input("Press enter to continue...")
            # Take and open a screenshot of the VM.
            case 13:
                if platform.system() != "Windows":
                    print("Sorry, this feature is only available on Windows.")
                    input("Press enter to continue...")
                    continue
                if State == "running":
                    try:
                        cwd = os.getcwd()
                        subprocess.run([VboxManagePath, "controlvm", CurrentVM, "screenshotpng", f"{cwd}\\screenshot.png"], check=True, stderr=subprocess.PIPE)
                        os.startfile(f"{cwd}\\screenshot.png")
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.decode("utf-8"))
                        print("Error occurred while taking screenshot, check above for details.")
                        input("Press Enter to continue...")
                else:
                    print("VM is not running.")
                    input("Press Enter to continue...")
            # Invalid operation number.
            case _:
                print("Please type a valid operation number.")
                input("Press enter to continue.")

if __name__ == "__main__":
    StartVirtualBoxVMController()