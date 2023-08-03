import time

def display():
    print("\nWelcome to Capacity Bank\n")
    time.sleep(0.5)
    welcome_infos = {0: 'Exit', 1: 'Create Account', 2: 'Display Account Info', 3: 'Deposit Fund', 4: 'Transfer Fund', 5: 'Reset Password'}
    users_info = {1: 'Agent', 2: 'Customer'}

    for key, value in users_info.items():
        print(f"Press {key} for {value}")

    while True:
        try:
            user_type = int(input("\nKindly pick an option: "))
            valid_inputs = [1, 2]
            if user_type in valid_inputs:
                break
            else:
                print("Invalid input; should be 1 or 2")
        except ValueError:
            print("Invalid input; please enter a number.")

    print("\nPick An Option To Proceed:")
    if user_type == 1:  # Agent
        valid_inputs = [0, 3, 5]
        for key, value in welcome_infos.items():
            if key in valid_inputs:
                print(f"Press {key} for {value}")
    else:  # Customer
        valid_inputs = [0, 1, 2, 4, 5]
        for key, value in welcome_infos.items():
            if key in valid_inputs:
                print(f"Press {key} for {value}")

    while True:
        try:
            selected_option = int(input("\nPick An Option To Proceed: "))
            valid_inputs = [i for i in range(len(welcome_infos))]
            if selected_option in valid_inputs:
                return selected_option
            else:
                print("Invalid input; should be in range of 0 - 5")
        except ValueError:
            print("Invalid input; please enter a number.")


# Example usage:
selected_option = display()
print("Selected option:", selected_option)

with open("main.py") as f:
  exec(f.read())   