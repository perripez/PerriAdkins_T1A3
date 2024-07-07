import json

def remove_item(file_path):
    """
    Allows user to input an item name to be removed from the JSON file
    """
    try:
        removed_item = input("Which item would you like to remove?: ").strip().lower()

        with open(file_path, 'r') as file:
            groceries = json.load(file)
        
        # Filter out the item to be removed
        updated_groceries = [item for item in groceries if item['item'].lower() != removed_item]

        # Check if any item was removed
        if len(updated_groceries) == len(groceries):
            print(f"Item '{removed_item}' not found in the list.")
        else:
            with open(file_path, 'w') as file:
                json.dump(updated_groceries, file, indent=4)
            print(f"Item '{removed_item}' removed from your list!")

            # Show updated list
            show_updated_list(file_path)

    except Exception as e:
        print(f"Sorry! An unexpected error has occurred: {e}")

def show_updated_list(file_path):
    """
    Display the updated list of items in the JSON file
    """
    try:
        with open(file_path, 'r') as file:
            groceries = json.load(file)
        
        print("Here's your updated Shopping list: ")
        for item in groceries:
            print(f"* {item['item']}")
            
        print(f"Don't forget to save your list!")

    except Exception as e:
        print(f"Sorry! An unexpected error has occurred: {e}")

