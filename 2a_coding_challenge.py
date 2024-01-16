import pyinputplus as pyip

# 2a Coding Challenge

# Initialising the arrays
account = []
accDetails = []

# Getting the acount ID
def get_ID():
    user_id = pyip.inputNum(prompt="Please enter your user ID: ")

    if user_id in account and user_id in accDetails:
        print("Valid ID")
        return user_id
    
    else:
        print("Invalid ID")
        get_ID()

# Checking the user
def check_credentials(user_id):
    user_name = pyip.inputStr(prompt="Please enter your user name: ")
    password = pyip.inputStr(prompt="Please enter your password: ")

    # Getting the valid account details
    valid_userName = account[user_id, 1]
    valid_password = account[user_id, 2]

    if user_name == valid_userName and password == valid_password:
        print("Valid credentials, logging in...")
    
    else:
        print("Invalid credentials, please try again...")
        check_credentials(user_id)

# Calling the functions
user_id = get_ID()
check_credentials(user_id)

# Displaying the menu with options
def display_option_menu(user_id):
    user_choice = pyip.inputMenu(["display balance", "withdraw money", "deposit money", "exit"])

    user_balance = accDetails[user_id, 1]
    over_draft_limit = accDetails[user_id, 2]
    withdrawal_limit = accDetails[user_id, 3]

    if user_choice == "4":
        quit()

    elif user_choice == "1":
        print(user_balance)

    elif user_choice == "2":
        withdrawal_value = pyip.inputNum(prompt="How much money would you like to withdraw? ")
        if withdrawal_value < withdrawal_limit and user_balance > over_draft_limit:
            user_balance -= withdrawal_value
            print("Transaction complete!")
            print(f"New balance: {user_balance}")
    
    elif user_choice == "3":
        deposit_value = pyip.inputNum(prompt="How much money would you like to deposit? ", min=10)
        user_balance += deposit_value
        print(f"New balance {user_balance}")

# Calling the display option menu function
display_option_menu(user_id)
