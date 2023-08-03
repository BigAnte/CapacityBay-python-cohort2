import random
from datetime import datetime


def creat_acct():
    new_account = {}
    account_details = ['Name', 'Age', 'Address', 'BVN', 'Email','Phone', 'password']

    for account_detail in account_details:
        detail = input(f"Kindly enter {account_detail}: ")
        new_account[account_detail] = detail

    random_number = random.randint(100000000, 999999999)
    acct_no = "3" + str(random_number)
    new_account["Account Number"] = acct_no
    new_account["created At"] = datetime.now()
    new_account["Account Balance"] = 0

    for key, value in new_account.items():
        print(key, ':', value)
    print(f'\n Welcome to capacity Bank; Your Account Number Is :  {acct_no} created at {datetime.now()} \n')
    #To get the customer email for reset purpose
    file_name = new_account['Email'] + '.txt'

    with open(file_name, 'w' ) as file:
        for key, value in new_account.items():
            file.write(f'{key} : {value}\n')


with open("main.py") as f:
  exec(f.read())   

# creat_acct()
