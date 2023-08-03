def customers_display():
  Email = input("\nEnter Your Email: ")
  try:
    Email = Email + '.txt'
    with open(Email, 'r') as file:
      info = file.read()
      print(info)
  except:
    print("Invalid Email")


with open("main.py") as f:
  exec(f.read())   

# customers_display()