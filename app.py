import os
import sys
import random


def menu_one():
    print("1. Staff Login\n2. Close app")

    # validate input
    try:
        get_input = int(input(": "))
    except Exception as err:
        print("Enter valid input")
        menu_one()
    if get_input > 2 or get_input < 1:
        print("\nEnter valid input\n")
        menu_one()

    if get_input == 1:
        staff_login()

    print("Thank you for banking with us, Goodbye!")
    sys.exit(0)


def menu_two():
    print("Select an option\n")
    print("1. Create New Bank Account\n2. Check Account Details\n3. Logout")

    # validate input
    try:
        get_input = int(input(": "))
    except Exception as err:
        print("Enter valid input")
        menu_two()
    if get_input > 3 or get_input < 1:
        print("\nEnter valid input\n")
        menu_two()
    if get_input == 1:
        create_account()
    elif get_input == 2:
        check_acct_details()
    return staff_logout()


def staff_is_validated(username, password):
    try:
        f = open("staff.txt")
    except IOError as e:
        print("Error opening file", e)
    else:
        lines = f.readlines()

        # create a new array to store the lines without new-line character
        line = []
        for l in lines:
            line.append(l.rstrip("\n"))

        # check if username and password match with the corresponding lines in staff.txt
        if username == line[0] and password == line[1]:
            print("Login successful!\n")
            return True
        elif username == line[5] and password == line[6]:
            print("Login successful!\n")
            return True
        else:
            print("Incorrect username or password, try again")
            return False
    finally:
        f.close()


def staff_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if staff_is_validated(username, password):

        # create session
        with open("session.txt", "w") as f:
            f.write(f"Logged In User: {username}")
        print(f"Welcome {username}! What do you want to do?\n")

        return menu_two()

    staff_login()


def staff_logout():
    if os.path.exists("session.txt"):
        os.remove("session.txt")
    print("Logged out!")
    print("Thank you for banking with us, Goodbye!")
    sys.exit(0)


# validate account number to check account details
def valid_acct_number(acct_number):
    try:
        f = open("customer.txt")
    except IOError as e:
        print("Error opening file", e)
    else:
        lines = f.readlines()
        details = []
        for l in lines:
            details.append(l.rstrip("\n"))

        # check if account number matches with the corresponding user's account number in customer.txt
        if f"Account Number: {str(acct_number)}" in details:
            return True
        else:
            print("Invalid account number, try again\n")
            return False
    finally:
        f.close()


def check_acct_details():
    try:
        acct_number = int(input("Enter your account number: "))
    except Exception as err:
        print("\nInvalid account number, try again\n")
        check_acct_details()

    # call function to valid account number. Function returns boolean
    if valid_acct_number(acct_number):
        try:
            f = open("customer.txt")
        except IOError as e:
            print("Error opening file", e)
        else:
            lines = f.readlines()
            details = []
            for l in lines:
                details.append(l.rstrip("\n"))

            # check the array of customer details and get the account number with a match
            # and prints the respective details
            for i in range(len(details)):
                if details[i] == f"Account Number: {acct_number}":
                    print("\n---------------------------------------")
                    print("\t   Account Details")
                    print("-----------------------------------------")
                    print(
                        f"\n{details[i+1]}\n{details[i]}\n{details[i+2]}\n{details[i+3]}\n{details[i+4]}\n"
                    )
                    print("-----------------------------------------")
                    break
        finally:
            f.close()

    return menu_two()


def email_does_not_exist(email):
    try:
        f = open("customer.txt")
    except IOError as e:
        print("Error opening file", e)
    else:
        lines = f.readlines()
        details = []
        for l in lines:
            details.append(l.rstrip("\n"))

        # validate if email already belongs to a user
        if f"Account Email: {email}" not in details:
            return True
        else:
            print("An account with that email already exist, use another email\n")
            return False
    finally:
        f.close()


def create_account():
    acct_name = input("Enter your account name: ")

    try:
        opening_balance = int(input("Enter your opening balance: "))
    except Exception as err:
        print("\nInput not valid, try again\n")
        create_account()

    acct_type = input("Enter the account type (Savings or Current): ")
    acct_email = input("Enter your account email: \n")
    labels = ["Account Name", "Opening Balance", "Account Type", "Account Email"]
    customer_data = [acct_name, opening_balance, acct_type, acct_email]

    # call function to check if the email exists. Function returns boolean
    if email_does_not_exist(acct_email):
        print("\nAccount Created!")

        # generate account number for current user
        numbers = "0123456789"
        rand_numbers = "".join(random.choices(numbers, k=8))
        acct_number = "40" + rand_numbers

        # save new user details to customer.txt
        with open("customer.txt", "a") as f:
            f.write(f"Account Number: {acct_number}\n")
            for (name, data) in zip(labels, customer_data):
                f.write(f"{name}: {data}\n")
            f.write("\n")

        print(f"\nYour account number is {acct_number}\n")
        return menu_two()
    create_account()


def main():
    print("Welcome to my banking system. Please choice an option\n")

    # call first menu options
    menu_one()


main()
