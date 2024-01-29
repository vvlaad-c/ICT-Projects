import pyinputplus as pyip

# 2a Coding Challenge

# Initialising the arrays
account = []
accDetails = []

# Getting the acount ID
def get_ID():
    user_id = pyip.inputNum(prompt="Please enter your user ID: ")

    if user_id in [row[0] for row in account] and user_id in [row[0] for row in accDetails]:
        print("Valid ID")
        return user_id
    else:
        print("Invalid ID")
        return get_ID()

# Checking the user
def check_credentials(user_id):
    user_name = pyip.inputStr(prompt="Please enter your user name: ")
    password = pyip.inputStr(prompt="Please enter your password: ")

    # Getting the valid account details
    valid_userName = account[user_id][1]
    valid_password = account[user_id][2]

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
    while True:
        user_choice = pyip.inputMenu(["display balance", "withdraw money", "deposit money", "exit"])

        if user_choice == "4":
            quit()

        elif user_choice == "1":
            print(accDetails[user_id][1])

        elif user_choice == "2":
            withdrawal_value = pyip.inputNum(prompt="How much money would you like to withdraw? ")
            if withdrawal_value < accDetails[user_id][2] and accDetails[user_id][1] > accDetails[user_id][3]:
                accDetails[user_id][1] -= withdrawal_value
                print("Transaction complete!")
                print(f"New balance: {accDetails[user_id][1]}")

        elif user_choice == "3":
            deposit_value = pyip.inputNum(prompt="How much money would you like to deposit? ", min=10)
            accDetails[user_id][1] += deposit_value
            print(f"New balance {accDetails[user_id][1]}")

# Calling the display option menu function
display_option_menu(user_id)
