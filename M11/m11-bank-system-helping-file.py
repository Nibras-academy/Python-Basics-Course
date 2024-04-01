# Define global variables
accounts = {}  # Dictionary to store account information {account_number: balance}

# Function to create a new account
def create_account():
    # Prompt user for account number and initial balance
    # Add new account to the accounts dictionary

# Function to deposit money
def deposit():
    # Prompt user for account number and amount to deposit
    # Add deposited amount to the account balance

# Function to withdraw money
def withdraw():
    # Prompt user for account number and amount to withdraw
    # Subtract withdrawn amount from the account balance

# Function to check balance
def check_balance():
    # Prompt user for account number
    # Display the current balance of the account

# Main function to run the bank management system
def main():
    # Display welcome message and menu options
    # Continuously prompt user for menu choice
    # Based on user's choice, call corresponding function
    # Repeat until user chooses to quit

if __name__ == "__main__":
    main()


def create_account():
    """
    This function allows the user to create a new bank account.
    
    It prompts the user to enter their account number and initial balance.
    If the account number is not already in use, it adds the new account to the accounts dictionary.
    If the account number already exists, it displays a message indicating that the account already exists.
    """
    print("\nCreate New Account")
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        print("Account already exists.")
    # Rest of the code   
    # Rest of the code    
    # Rest of the code    
    # Rest of the code    

    