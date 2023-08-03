from creat_acct import creat_acct
from display_info import display
from deposit import my_deposit
from transfer_fund import  my_transfer_funds
from reset import reset_pasword
from customers_info import customers_display
from exit import exit


myinput= display()
if myinput == 0:
    exit()
elif myinput == 1:
    creat_acct()
elif myinput == 2:
    customers_display()
elif myinput == 3:
    my_deposit()
elif myinput == 4:
   my_transfer_funds()
elif myinput == 5:
    reset_pasword()



