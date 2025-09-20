import hashlib
import math 
import csv
import re
# This is my exception that shows how entry of wrong password is to be dealt with . 

class LoginDetailsError(Exception) :
    def __init__(self, alert = "You have entered the wrong username or password"):
     super().__init__(f"{alert}")

# Here we have exceptions for errors while carrying out transactions 
class BankError(Exception): pass
class InsufficientFundsError(BankError): pass


    
    # This section shows how passwords are encrypted using hashing from the hashlib module
    # in addition to hashing there is an addition of pi to the encryption which adds to hashing to make passwords even safer
def hashing_with_pi(password):
    salted = password + str(math.pi)  
    hashed = hashlib.sha256(salted.encode()).hexdigest()
    return hashed


#The user enters their username and password when creating an account which is then
#stored in an external csv file to ensure user details remain even after the program stops running.

def account_creation() :
    
    correct_username = input("Create your username :")
    correct_password = input("Create your password :")
    hashed =hashing_with_pi(correct_password)
    with open ("user_details.csv" , "a", newline="",) as f :
        writer = csv.writer(f)
        writer.writerow([correct_username, hashed])
    return correct_username  , hashed

  
# The login phase which involves users entering their username; and password which is then hashed and 
# cross-examined against the ones they gave during account cretaion.
# If they match:
#     AccessGranted
#  else:
#     AccessDenied

def login() :
  for i in range (3) :
    username = input("Enter your username :")
    login_password = input("Enter your password :")
    new_hash =hashing_with_pi(login_password)
    with open("user_details.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            correct_username, hashed = row
            if username == correct_username and  new_hash == hashed :
              print("Login succesful, Welcome to GreenPeak")
              return True
            else: 
              print("Invalid login details, try again")
        
         
   
    return username , login_password , new_hash
 

    

# A savings system whereby you can only withdraw when you reach a certain amount
#  unlike normal savings schemes that involve time.
# This ensures you cannot touch the money until you reach your targeted savings first. 

def withdrawing_from_savings():
 target_savings =int(input("What is your targeted savings : "))
 if savings > target_savings :
      amount_to_be_withdrawn=int(input("How much would you like to withdraw:"))
 if amount_to_be_withdrawn <= savings:
          savings -= amount_to_be_withdrawn
          print(f"You withdrew{amount_to_be_withdrawn} succesfully and your new balance is{savings}")
        
          
 else :
       print("You cannot withdraw until you reach your target amount.")
 return target_savings


def displayAccountBalance() :
   print(f"Your account balance is {account_balance}")

def displaySavingsBalance() :
   print(f"You have saved {savings} so far , still {target_savings - savings} to go")

# This is the initial menu on starting the program 
# which lets you choose between first creating an account or logging in    
print("This is GreenPeak Banking,Hello")
choice =int (input("Select 1 for account creation or 2 for login"))


if choice == 1 :
    account_creation() 
    login()
elif choice == 2 :
   login()
account_balance = 0
savings = 0
target_savings = 0

#This is where it gets interesting.You need to enter your command wwhich involves entering 2 parts;
# which transaction would you like to do and the amount to transact.

while True:
  command = input("Hello,what would you like to do for now😊:")
  prior_amount= re.findall(r"\d+",command)

  amount = int (prior_amount[0]) if prior_amount else 0

  #This section takes your transaction type and amount and carries it out.
 
 
  if "exit" in command.lower() :
   print("Goodbye , see you next time")
   exit()

  
   if "withdraw" in command.lower() :
    account_balance -= amount
    print(f"{amount} has been succesfully withdrawn")
  
  if "deposit" in command.lower():
   account_balance += amount
   print(f"{amount} has been succesfully deposited" )
  
  if "save" in command.lower():
   savings += amount
   print(f"{amount} has been succesfully saved")
  
  if "withdraw from savings" in command.lower():
     withdrawing_from_savings()

   
   
   
   

  




