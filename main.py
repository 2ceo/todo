import os 
import sys
import subprocess

def menu():
    os.system("clear")
    print("1. Add a note 4. Rain\n2. My notes\n3. Exit")
    
# ------------------------------  PLAYER   -----------------------------

def mpvPlayer(userInput):
    if userInput == "4":
        subprocess.run(
            ["mpv", "--quiet", "--audio-device=pulse", "--loop", "sound/ambience-rain.wav"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
# ----------------------------   ADD NOTES   ---------------------------

def addNote(userInput, notes):
    os.system("clear")
    print("1. Back 2. Save note")
    print("Write your note")    
    userInput = input()
    notes.append(userInput)
    print(notes)
    if userInput == "1":
        menu()

# ----------------------------  WATCH NOTES  ----------------------------

def watchNote(userInput):
    os.system("clear")
    print("1. Back 2. Save note")
    print("Here will be your notes")
    userInput = input()
    if userInput == "1":
        menu()
    if userInput == "2":
        os.system("clear")
        print("Note saved")
    else:
        menu()

# ------------------------------    EXIT   ------------------------------

def exit(userInput):
    os.system("clear")
    print("Are you sure?\n1. Yes 2. No")
    userInput = input()
    if userInput == "1":
        sys.exit()
        return False
    if userInput == "2":
        menu()

# ------------------------------    MAIN   ------------------------------

def main():
    notes = []
    menu()
    while True:
        userInput = input()
        if userInput == "1":   # Add notes
            addNote(userInput, notes)
        if userInput == "2":   # View notes
            watchNote(userInput)
        if userInput == "3":
            exit(userInput)
        if userInput == "4":
            mpvPlayer(userInput)

if __name__ == "__main__":
    main()
