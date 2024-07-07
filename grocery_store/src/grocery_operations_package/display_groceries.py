def display_groceries(groceries):
    """
    Display list of groceries from JSON file
    """
    try:
        for item in groceries:
            print(f"{item["item"]} | {item["price"]}")
    except KeyError as e:
        print(f"Uh oh... error displaying groceries: missing key {e}")
    except Exception as e:
        print(f"Sorry! An unexpected error has occured: {e}")