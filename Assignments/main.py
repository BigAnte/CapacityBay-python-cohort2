# simple python program that uses input from users to print out  following response
#  print not allowed if score is above 100, less than zero or alphabet, print A if score is
# grater that 69, print B if score is greater than 59 and less than 70 ,  print C if score
# is greater than 49 and less than 60 ,  print D if score is greater than 39 and less than 50 ,
#   print E if score is greater than 29 and less than 40 ,  print F if score is greater than 30

# Recieve input from the user
score = input("Enter your score: ")

# Check if input is not a number
if not score.isnumeric():
    print("Not allowed")
elif int(score) > 100 or int(score) < 0:
    print("Not allowed")
elif int(score) > 69:
    print("A")
elif int(score) > 59 and score < 70:
    print("B")
elif int(score) > 49 and score < 60:
    print("C")
elif int(score) > 39 and score < 50:
    print("D")
elif int(score) > 29 and score < 40:
    print("E")
else:
    print("F")
