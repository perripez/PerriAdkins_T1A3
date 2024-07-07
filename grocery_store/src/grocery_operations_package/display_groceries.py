import json

def display_groceries(file_path):
    """
    Display list of groceries from JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            groceries = json.load(file)
            print("\nList of Items:")
            for item in groceries:
                print(f"- {item['item']} | {item['price']}")
                
    except Exception as e:
        print(f"Sorry! An unexpected error has occurred: {e}")