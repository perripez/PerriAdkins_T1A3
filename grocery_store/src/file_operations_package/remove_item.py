# Import JSON to be read by functions
import json

def save_groceries(file_path, groceries):
    """
    Saves groceries to JSON file - this has been added to ensure that the most recent JSON file is always read.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(groceries, file, indent=4)
        print(f"Your grocery list was saved to {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred while saving: {e}")


def remove_item(file_path):
    """
    Allows user to input an item name to be removed from the JSON file.
    """
    try:
        removed_item = input("Which item would you like to remove?: ").strip().lower() # Take user input to remove their desired item

        with open(file_path, 'r') as file:
            groceries = json.load(file) # Load existing file

        # Filter out the item to be removed
        updated_groceries = [item for item in groceries if item['item'].lower() != removed_item]

        # Check if any item was removed
        if len(updated_groceries) == len(groceries):
            print(f"Item '{removed_item}' not found in the list.")
        else:
            save_groceries(file_path, updated_groceries)
            print(f"Item '{removed_item}' removed from your list!")

    except Exception as e:
        print(f"Sorry! An unexpected error has occurred: {e}")
