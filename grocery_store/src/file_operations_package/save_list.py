# Import JSON to be read by functions
import json

def save_groceries(file_path, groceries):
    """
    Saves groceries to JSON file
    
    paraneters: file_path: Path to the JSON file, groceries: items in JSON file
    return: success message if save is successful
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(groceries, file, indent=4) # .dump stores items in file with indent set to 4
        print(f"Yahoo! Your grocery list was saved to {file_path}")
    except PermissionError:
        print(f"Stop right there! Permission denied to write.")
    except Exception as e:
        print(f"Argh! An unexpected error has occured: {e}")
        