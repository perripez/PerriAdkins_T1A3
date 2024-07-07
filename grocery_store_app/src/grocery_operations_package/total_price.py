def total_price(groceries):
    """
    Calculate total price of all items in JSON file
    """
    try:
        total = sum(item["price"] for item in groceries) # sum = adding price together for each
        rounded_total = round(total, 3)
        return rounded_total
    except KeyError as e:
        print(f"Whoops! Error calculating total: Missing key {e}")
        return 0
    except TypeError:
        print("Cannot calculate total: Invalid item data.")
    except Exception as e:
        print(f"Argh! An unexpected error has occured: {e}")
        return 0


