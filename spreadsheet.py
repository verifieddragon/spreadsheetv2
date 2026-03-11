import os

###############################################################################################
# Main spreadsheet menu and user interaction
###############################################################################################

def startSpreadsheet():
    """Start the spreadsheet menu and handle user interactions."""
    spreadsheet_name = spreadsheetName()
    print(f"Spreadsheet '{spreadsheet_name}' is now active.")
    sheet = openFile(spreadsheet_name)
    
    menuActive = True
    while menuActive:
        print("\n\nSpreadsheet Menu")
        print("-" * 40)
        print("\n1. Add an item")
        print("2. Remove an item")
        print("3. View spreadsheet")
        print("4. Save and return to main menu\n\n\n")
        
        choice = input("Enter your choice: ")
        
        if choice == '1': # Add an item and view the spreadsheet after
            item_name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: $"))
            sheet.add_item(item_name, quantity, price)
            print("Item added successfully.")
            sheet.view_spreadsheet()
            
        elif choice == '2': # Remove an item and view the spreadsheet after
            sheet.view_spreadsheet()
            index = (int(input("Enter the index of the item to remove (starting from 1): ")) - 1)
            try:
                sheet.remove_item(index)
                print("Item removed successfully.")
            except IndexError:
                print("Invalid index. Please try again.")
            sheet.view_spreadsheet()
            
        elif choice == '3': # View the spreadsheet
            sheet.view_spreadsheet()
        
        elif choice == '4': # Save and return to main menu
            print(f"Saving '{spreadsheet_name}' and returning to main menu.")
            saveFile(sheet)
            menuActive = False
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def spreadsheetName():
    """Prompt the user for a spreadsheet name and handle file creation if it doesn't exist."""
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
                    createFile(userinputname)
                    print(f"Spreadsheet '{userinputname}' created.")
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

###############################################################################################
# File handling functions
###############################################################################################

def openFile(name):
    """Open the spreadsheet file and read its contents into a spreadsheet instance."""
    sheet = spreadsheet(name)
    with open(name, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip header row
            if line.strip():  # Skip empty lines
                parts = line.strip().split('|')
                if len(parts) >= 3:
                    item_name, quantity, price = parts[0], int(parts[1]), float(parts[2])
                    sheet.add_item(item_name, quantity, price)
    return sheet

def createFile(name):
    """Create a new spreadsheet file with the given name."""
    with open(name, 'w') as file:
        file.write("Name|Quantity|Price|Total\nEmpty Spreadsheet")

def saveFile(sheet):
    """Save the spreadsheet data to the file."""
    with open(sheet._spreadsheet__name, 'w') as file:
        file.write("Name|Quantity|Price|Total\n")  # Write header row
        for item in sheet._spreadsheet__items: # Write each item as a line in the file
            file.write(f"{item.name}|{item.quantity}|{item.price}|{item.total}\n")

def findFile(name):
    """Search for the spreadsheet file in the current directory."""
    for file in os.listdir('.'):
        if file == name:
            return name
    return None

###############################################################################################
# Spreadsheet and rowItem classes
###############################################################################################

class spreadsheet:
    def __init__(self, name):
        self.__name = name
        self.__items = []

    def add_item(self, name, quantity, price):
        """Add a new rowItem to the spreadsheet."""
        item = rowItem(name, quantity, price)
        self.__items.append(item)

    def remove_item(self, index):
        """Remove an item by index."""
        if 0 <= index < len(self.__items):
            del self.__items[index]
        else:
            raise IndexError("Index out of range.")

    @property
    def grand_total(self):
        """Calculate and return the grand total of all items."""
        return sum(item.total for item in self.__items)

    def view_spreadsheet(self):
        """Display the contents of the spreadsheet."""
        print(f"\nSpreadsheet: {self.__name}")
        print("-" * 55)
        print(f"{'Name':<20} | {'Qty':<5} | {'Price':<10} | {'Total':<10}")
        print("-" * 55)
        for item in self.__items:
            print(item)
        print("-" * 55)
        print(f"{'Grand Total':<41} | {self.grand_total:<10.2f}\n")
        print("x" * 55)


class rowItem:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__total = (quantity * price)
        
    @property
    def name(self):
        """Get the name of the item."""
        return self.__name
    @name.setter
    def name(self, value):
        """Set the name of the item."""
        self.__name = value


    @property
    def quantity(self):
        """Get the quantity of the item."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        """Set the quantity of the item and updates the total."""
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value
        self.__total = value * self.__price  # Update total whenever quantity changes


    @property
    def price(self):
        """Get the price of the item."""
        return self.__price

    @price.setter
    def price(self, value):
        """Set the price of the item and updates the total."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value
        self.__total = self.__quantity * value  # Update total whenever price changes

    @property
    def total(self):
        """Get the total price of the item."""
        return self.__total
    

    def __str__(self):
        """Return a formatted string representation of the row item."""
        return f"{self.__name:<20} | {self.__quantity:<5} | {self.__price:<10.2f} | {self.__total:<10.2f}"
    