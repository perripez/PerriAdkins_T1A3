def add_item(groceries):
    """
    Allows user to input an item name + price to be added to the JSON file
    """
    try:
        item = input.lower("Please enter item to add to your list: ") # .lower to ensure inout formatting will match existing list
        price = float(input("Please enter item price: $")) # float to ensure cents (decimals) can be calulated from input

        grocery = {"item": item, "price": price}
        groceries.append(grocery) # .append to add to JSON file
        print("Yay! Item successfully added")
    except ValueError:
        print("Whoops! Price must be an integer silly")
    except Exception as e:
        print(f"Sorry! An unexpected error has occured: {e}")