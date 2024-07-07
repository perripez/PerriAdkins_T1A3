# Import JSON to be read by functions
import json

def save_groceries(file_path, groceries):
    """
    Saves groceries to JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(groceries, file, indent=4)
        
        print("Thanks for visiting!")
        print(f"Your grocery list was saved to {file_path}")

    except Exception as e:
        print(f"An unexpected error occurred while saving: {e}")

