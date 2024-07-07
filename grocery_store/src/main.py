import os # Clears console for user aftereach interaction for easy readability

import locale
locale.setlocale(locale.LC_ALL, '') # Formats pricing correctly

# Import functions from packages
from file_operations_package import load_groceries, save_list
from grocery_operations_package import add_item, display_groceries, total_price

FILE_PATH = '../data/grocery_list.json'

def clear_console():
    os.system("clear")

def main():
    clear_console()
    groceries = load_groceries.load_groceries(FILE_PATH)

    if not groceries:
        print("Yikes, no matches loaded or an error occured. Exiting")
        return
    while True: # While loop that allows user to retry an input if an error occurs
        print("\n Grocery Planner:")
        print("1. Check current list")
        print("2. Add item to list")
        print("3. Check out!")
        print("4. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            clear_console()
            display_groceries.display_groceries(groceries) # Call display groceries function
        elif choice == "2":
            clear_console()
            add_item.add_item(groceries) # Call add item function
        elif choice == "3":
            clear_console()
            print(f"Your total is: {locale.currency(total_price.total_price(groceries))}") # Call total price function & formats in $0.00
            print("Thank you for shopping with us!")
        elif choice == "4":
            clear_console()
            try:
                save_list.save_groceries(FILE_PATH, groceries) # Call save groceries function
                break
            except Exception as e:
                print(f"Damn... sorry your list was not saved: {e}")
        else:
            print("Very funny! Please choose an option")

if __name__ == "__main__":
    main()

