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


def my_transfer_funds():
    txt_files = get_txt_files_in_directory()

    if len(txt_files) < 2:
        print("Insufficient .txt files in the directory. Need at least two files.")
        return

    print("Available .txt files for accounts:")
    for index, file in enumerate(txt_files):
        print(f"{index + 1}. {file}")

    try:
        sender_index = int(input("Select your account (Enter the number): "))
        receiver_account_no = input("Enter the receiver's Account Number: ")

        if sender_index < 1 or sender_index > len(txt_files):
            print("Invalid selection.")
            return

        sender_file = txt_files[sender_index - 1]
        sender_details = read_account_details(sender_file)

        if not sender_details:
            return

        # Input from the user
        password = input("Enter your Password: ")
        Amount = float(input("Enter the Amount to transfer: "))

        # Check the password
        if sender_details['password'] != password:
            raise ValueError("Invalid password!")

        receiver_file = None
        for file in txt_files:
            account_details = read_account_details(file)
            if account_details and account_details.get('Account Number') == receiver_account_no:
                receiver_file = file
                break

        if not receiver_file:
            print(f"Receiver's account with Account Number '{receiver_account_no}' not found.")
            return

        # Perform the fund transfer
        current_balance = float(sender_details['Account Balance'])
        if current_balance < Amount:
            raise ValueError("Insufficient balance for transfer!")

        sender_details['Account Balance'] = str(current_balance - Amount)

        receiver_details = read_account_details(receiver_file)
        receiver_balance = float(receiver_details['Account Balance'])
        receiver_details['Account Balance'] = str(receiver_balance + Amount)

        # Update the sender's account file
        with open(sender_file, 'w') as file:
            for key, value in sender_details.items():
                file.write(f"{key} : {value}\n")

        # Update the receiver's account file
        with open(receiver_file, 'w') as file:
            for key, value in receiver_details.items():
                file.write(f"{key} : {value}\n")

        print("Fund transfer successful")
        print(f"Your new Account Balance: {current_balance - Amount}")
    except ValueError as e:
        print(str(e))


with open("main.py") as f:
  exec(f.read())   
# Call the function
# my_transfer_funds()


