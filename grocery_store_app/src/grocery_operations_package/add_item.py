# Import JSON to be read by functions
import json

def save_groceries(file_path, groceries):
    """
    Saves groceries to JSON file - this has been added to ensure that the most recent JSON file is always read.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(groceries, file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred while saving: {e}")


def add_item(file_path, groceries):
    """
    Allows user to input an item name + price to be added to the JSON file.
    """
    try:
        item = input("Please enter item to add to your list: ") 
        price = float(input("Please enter item price: $")) # float to ensure cents (decimals) can be calculated from input

        grocery = {"item": item.lower(), "price": price}
        groceries.append(grocery)
        
        save_groceries(file_path, groceries)  # Save the updated groceries list to the JSON file
        
        print("Yay! Item successfully added")
    except ValueError:
        print("Whoops! Price must be a number silly")
    except Exception as e:
        print(f"Sorry! An unexpected error has occurred: {e}")

    
    save_groceries(file_path, groceries)  # Save the updated groceries list to the JSON file
        