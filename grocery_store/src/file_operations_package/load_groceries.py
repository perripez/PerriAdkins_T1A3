# Import JSON to be read by functions
import json

def load_groceries(file_path):
    """
    Loads groceries from JSON file
    
    paraneters: file_path: Path to the JSON file
    return: List of grocery items OR an empty list if error occurs
    """
    try:
        with open(file_path,'r') as file:
            groceries = json.load(file) # read groceries from JSON file
        return groceries
    except FileNotFoundError:
        print(f"Uh oh! The file {file_path} is missing!)")
        return []
    except Exception as e:
        print(f"Argh! An unexpected error has occured: {e}")
        return []
    
