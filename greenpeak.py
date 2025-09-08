import hashlib
import math 
import csv


class LoginDetailsError(Exception) :
   def __init__(self, alert = "You have entered the wrong username or password"):
      super().__init__(f"{alert}")


class BankError(Exception): pass
class InsufficientFundsError(BankError): pass


try:
    raise InsufficientFundsError("Balance too low")
except BankError as e:   # 
    print("Bank error:", e)

    
    
def hashing_with_pi(password):
    salted = password + str(math.pi)  
    hashed = hashlib.sha256(salted.encode()).hexdigest()
    return hashed



def account_creation() :
    
    correct_username = input("Create your username :")
    correct_password = input("Create your password :")
    hashed =hashing_with_pi(correct_password)
    with open ("user_details.csv" , "a", newline="",) as f :
        writer = csv.writer(f)
        writer.writerow([correct_username, hashed])
    
    return correct_username  , hashed

  

try :
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
            
    print("Invalid login details, try again")
    return False 
        
    return username , login_password , new_hash
  
  raise LoginDetailsError

except(LoginDetailsError) as e :
     print(e)
 
def withdrawing_from_savings():
    target_savings =int(input("What is your targeted savings : "))
    if savings > target_savings :
       amount_to_be_withdrawn=int(input("How much would you like to withdraw:"))
       withdrawn_savings_amount = 0
       withdrawn_savings_amount -= (savings - amount_to_be_withdrawn)

    
    
 
    
print("This is GreenPeak Banking,Hello")
choice =int (input("Select 1 for account creation or 2 for login"))

if choice == 1 :
    account_creation() 
    login()

elif choice == 2 :
   login()

account_balance = 0
savings = 0
command = input("Enter what you would like to do kindly,remember it need to have 2 areas , the action and amount : ")

parts = command.split()
action = parts[0].lower()
amount = int (parts[1])


if command.lower() == "exit" :
   exit()
   print("Goodbye")

if parts[0] == "deposit" :
   account_balance += amount 
   raise InsufficientFundsError
   print(f"{amount} has been succesfully deposited" )

elif parts[0] == "withdraw" :
   account_balance -= amount
   raise InsufficientFundsError
   print(f"{amount} has been succesfully withdrawn")


elif parts[0] == "save" :
   savings += amount
   raise InsufficientFundsError
   print(f"{amount} has been succesfully saved")

   

   
   

  




