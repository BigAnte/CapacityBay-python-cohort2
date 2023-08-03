import os

def read_account_details(filename):
    account_details = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(' : ')
                account_details[key] = value
    except FileNotFoundError:
        print(f"Account file '{filename}' not found.")
        return None
    except ValueError:
        print("Invalid file format.")
        return None

    return account_details


def get_txt_files_in_directory():
    txt_files = []
    for file in os.listdir():
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files


def my_deposit():
    txt_files = get_txt_files_in_directory()

    if len(txt_files) == 0:
        print("No .txt files found in the directory.")
        return

    print("Available .txt files for accounts:")
    for index, file in enumerate(txt_files):
        print(f"{index + 1}. {file}")

    try:
        selected_index = int(input("Select your account (Enter the number): "))

        if selected_index < 1 or selected_index > len(txt_files):
            print("Invalid selection.")
            return

        full_account_file = txt_files[selected_index - 1]

        account_details = read_account_details(full_account_file)

        if not account_details:
            return

        # Input from the user
        Email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        account_no = input("Enter your Account Number: ")
        Amount = float(input("Enter your Amount: "))

        # Check email and account number
        if account_details['Email'] != Email:
            raise ValueError("Invalid email")
        if account_details['Account Number'] != account_no:
            raise ValueError("Invalid account number!")

        # Check the password
        if account_details['password'] != password:
            raise ValueError("Invalid password!")

        # Update the account balance
        current_balance = float(account_details['Account Balance'])
        new_balance = current_balance + Amount
        account_details['Account Balance'] = str(new_balance)

        # Write the updated account balance back to the file
        with open(full_account_file, 'w') as file:
            for key, value in account_details.items():
                file.write(f"{key} : {value}\n")

        print("Deposit successful")
        print(f"New Account Balance: {new_balance}")
    except ValueError as e:
        print(str(e))



# my_deposit()



with open("main.py") as f:
  exec(f.read())   