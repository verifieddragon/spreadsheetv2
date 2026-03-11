######################################################################
# Spreadsheet Program v2
# by Kolby Miller
#
# Program creates simple spreadsheets for items, prices, and
# quantities. 
#
######################################################################

import spreadsheet

def initMenu():
    active = True
    while active:
        print("\n\nWelcome to the spreadsheet program!")
        print("-" * 40)
        print("\n1. Create or open a spreadsheet")
        print("2. Exit\n\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            spreadsheet.startSpreadsheet()
        elif choice == '2':
            print("Exiting the program.")
            active = False
            return "Done"
        else:
            print("Invalid choice. Please enter 1 or 2.")
    

def main():
    initMenu()
    
    


if __name__ == "__main__":    main()