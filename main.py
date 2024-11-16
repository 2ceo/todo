import os 
import sys
import subprocess
import signal
import time 
# import platform # for future support windows

def menu():
    os.system("clear")
    print("1. Add a note 4. Sound\n2. My notes\n3. Exit")
    
# ------------------------------  PLAYER   -----------------------------

def mpvPlayer(userInput):
    os.system("clear")
    print("1. Menu 4-7. Back Play  0. Stop\n4. Rain 5. Thunder 6. Fire 7. Wind\n-----------------------------------")
    userInput = input()
    if userInput == "0":
        os.system("pkill mpv")
        print("ok")
        time.sleep(2)
        menu()
        
    if userInput == "4":
        os.system("clear")
        menu()
        subprocess.Popen(
            ["mpv", "--quiet", "--audio-device=pulse", "--loop", "sound/ambience-rain.wav"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    if userInput == "5":
        os.system("clear")
        menu()
        subprocess.Popen(
            ["mpv", "--quiet", "--audio-device=pulse", "--loop", "sound/ambience-thunder.wav"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    if userInput == "6":
        os.system("clear")
        menu()
        subprocess.Popen(
            ["mpv", "--quiet", "--audio-device=pulse", "--loop", "sound/ambience-fire.wav"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    if userInput == "7":
        os.system("clear")
        menu()
        subprocess.Popen(
            ["mpv", "--quiet", "--audio-device=pulse", "--loop", "sound/ambience-wind.wav"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    if userInput == "1":
        menu()


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

def exitProgram(userInput):
    os.system("clear")
    print("Are you sure?\n1. Yes 2. No")
    userInput = input()
    if userInput == "1":
        os.system("pkill mpv")
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
            exitProgram(userInput)
        if userInput == "4":
            mpvPlayer(userInput)

if __name__ == "__main__":
    main()
