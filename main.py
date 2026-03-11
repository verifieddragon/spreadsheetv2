######################################################################
# Spreadsheet Program v2
# by Kolby Miller
#
# Program creates simple spreadsheets for items, prices, and
# quantities. 
#
######################################################################

import spreadsheet
import os

def startSpreadsheet():
    spreadsheet_name = spreadsheetName()
    print(f"Spreadsheet '{spreadsheet_name}' is now active.")
    #Call spreadsheet.py functions here to manipulate the spreadsheet as needed.
    

def initMenu():
    active = True
    while active:
        print("\nWelcome to the spreadsheet program!")
        print("-" * 40)
        print("\n1. Create or open a spreadsheet")
        print("2. Exit\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            startSpreadsheet()
        elif choice == '2':
            print("Exiting the program.")
            active = False
            return "Done"
        else:
            print("Invalid choice. Please enter 1 or 2.")
    

def spreadsheetName():
    namenotGood = True
    while namenotGood:
        userinputname = input("Enter the name of the spreadsheet: ")
        if findFile(userinputname) == None:
            valid_input = False
            while not valid_input:
                usercreate = input(f"Spreadsheet '{userinputname}' not found. Create it? (y/n): ").strip().lower()
                if usercreate == 'y':
                    valid_input = True
                    namenotGood = False
                    return userinputname
                elif usercreate == 'n':
                    valid_input = True
                    print("Please enter a different name.")
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    valid_input = False
        else:
            print(f"Spreadsheet '{userinputname}' found.")
            return userinputname
    

def findFile(name):
    """Search for the spreadsheet file in the current directory."""
    for file in os.listdir('.'):
        if file == name:
            return file
    return None

def main():
    initMenu()
    
    


if __name__ == "__main__":    main()