def reset_pasword():
  print("Enter your email to reset the pasword")
  Email = input("Enter your email: ")
  try:
    Email = Email + '.txt'
    with open(Email, 'r+') as file:
      lines = file.readlines()
      last_line = lines[-1].strip()

      new_password = input("Enter your new Password: ")
      lines[-4] = f'Password: {new_password}\n'

      with open(Email, 'w') as file:
        file.writelines(lines)
        print("\nPassword resets successfully!")
  except:
    print("invalid Email!!!")


# reset_pasword()
with open("main.py") as f:
  exec(f.read())   