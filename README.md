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



