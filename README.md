# PerriAdkins_T1A3

# Documentation

[GitHub Repo](https://github.com/perripez/PerriAdkins_T1A3)

## About the App

__Purpose:__

A grocery list app that a user can view/input items to be saved to a list. Terminal outputs will replicate checking out in a grocery store for user experience.

__Features:__

While Loop - Main menu that cycles through options and displays original prompt to user again if an error occurs

Variables - ```<item_name>``` and ```<item_price>``` can be manipulated by the user through funtions eg. add/remove

Conditional Control Statements - if, elif and else statements used when user selects from 1-5 in main menu & try and except statements used to determine is user input is valid or not

Error Handling - User friendly messages will be printed to the user when an error occcurs eg. ```"Whoops! Please enter a number between 1-5"```

__Functionality__:

App will ask the user to select an option from these options:

1. *DISPLAY GROCERY LIST*
Function that reads an existing JSON file and lists items and their respective prices (dicionary style with keys)

2. *ADD TO GROCERY LIST*
User is prompted to enter details of item they wish to add to the list:
```<item_name>, $<item_price>``` 
For example:
```"Carrots", $"2"```

- If successful, app will add item to existing JSON file and print a success message for the user

- If unsuccessful, app will print an error
User is prompted for input again

3. *REMOVE FROM GROCERY LIST*
User is prompted to enter item they wish to remove from the list:
```<item_name>```
For example:
```"Carrots"```

- If successful (item is in the list), app will remove item from existing JSON file and print a success message for the user

- If unsuccessful, app will print an error 
User is prompted for input again

4. *CHECKOUT*
Function that adds the price of all items and prints the total price to the user:

```"Thank you for shopping with us! Your total is $<total_price>"``` __~__

5. *SAVE AND EXIT*
Function that saves the exiting JSON file date and exits the app

- If successful, app will save file, print file path for user to access and exit the app
- If unsuccessful, app will print and error
User is prompted for input again

### More information about the app is documented help.txt file

## Flowchart

![Flowchart](./docs/Terminal%20App%20Flowchart.png)

## Psuedocode

```
BEGIN
    FUNCTION main
        WHILE True
            DISPLAY "Please select an option:"
            DISPLAY "1. DISPLAY GROCERY LIST"
            DISPLAY "2. ADD TO GROCERY LIST"
            DISPLAY "3. REMOVE FROM GROCERY LIST"
            DISPLAY "4. CHECKOUT"
            DISPLAY "5. SAVE AND EXIT"
            INPUT option

            IF option IS "1"
                CALL display_grocery_list()
            ELIF option IS "2"
                CALL add_to_grocery_list()
            ELIF option IS "3"
                CALL remove_from_grocery_list()
            ELIF option IS "4"
                CALL checkout()
            ELIF option IS "5"
                CALL save_and_exit()
                BREAK
            ELSE
                DISPLAY "Invalid option. Please try again."
            END IF
        END WHILE
    END FUNCTION

    FUNCTION display_grocery_list
        TRY
            READ grocery_list FROM "grocery_list.json"
            FOR EACH item IN grocery_list
                DISPLAY item.name + ": $" + item.price
            END FOR
        EXCEPT
            DISPLAY "Error reading grocery list."
    END FUNCTION

    FUNCTION add_to_grocery_list
        DISPLAY "Enter item name:"
        INPUT item_name
        DISPLAY "Enter item price:"
        INPUT item_price

        TRY
            READ grocery_list FROM "grocery_list.json"
            ADD item_name: item_price TO grocery_list
            WRITE grocery_list TO "grocery_list.json"
            DISPLAY "Item added successfully."
        EXCEPT
            DISPLAY "Error adding item to grocery list."
    END FUNCTION

    FUNCTION remove_from_grocery_list
        DISPLAY "Enter item name to remove:"
        INPUT item_name

        TRY
            READ grocery_list FROM "grocery_list.json"
            IF item_name IN grocery_list
                REMOVE item_name FROM grocery_list
                WRITE grocery_list TO "grocery_list.json"
                DISPLAY "Item removed successfully."
            ELSE
                DISPLAY "Item not found in grocery list."
            END IF
        EXCEPT
            DISPLAY "Error removing item from grocery list."
    END FUNCTION

    FUNCTION checkout
        TRY
            READ grocery_list FROM "grocery_list.json"
            total_price = 0
            FOR EACH item IN grocery_list
                total_price = total_price + item.price
            END FOR
            DISPLAY "Thank you for shopping with us! Your total is $" + total_price
        EXCEPT
            DISPLAY "Error calculating total price."
    END FUNCTION

    FUNCTION save_and_exit
        TRY
            WRITE grocery_list TO "grocery_list.json"
            DISPLAY "Grocery list saved successfully. File path: <file_path>"
        EXCEPT
            DISPLAY "Error saving grocery list."
    END FUNCTION

    CALL main
END
```
