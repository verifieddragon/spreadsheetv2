from spreadsheet import rowItem

def main():
    
    # Create a rowItem instance
    item1 = rowItem("Apple", 10, 0.5)
    
    # Display the item details
    print(item1)
    
    # Update quantity and price
    item1.quantity = 15
    item1.price = 0.75
    
    # Display the updated item details
    print(item1)
    print()
    print()
    
    
    
###########################################################################


    item2 = rowItem("Banana", 20, 0.3)
    item3 = rowItem("Orange", 5, 0.8)
    item4 = rowItem("Grapes", 8, 1.2)

    # Example table
    print(f"{'Name':<20} | {'Qty':<5} | {'Price':<10} | {'Total':<10}")
    print("-" * 50)
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    print("-" * 50)
    print(f"{'Total':<41} | {item1.total + item2.total + item3.total + item4.total:<10.2f}")
    print()
    
    
if __name__ == "__main__":    main()