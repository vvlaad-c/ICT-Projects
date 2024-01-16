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
    
