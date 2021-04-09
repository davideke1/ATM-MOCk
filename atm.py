from datetime import datetime

import random

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
userBalance = 1000000000.00

database = {
    1234567890: ["Eke@gmail.com", "David", "Uzoma", "Password"], # saved databse for registered users 
    9874561230: ["Henry@gmail.com", "Henry", "Kachi", "Password1"],
    2345678901: ["Peter@gmail.com", "Hery", "Martins", "password2"]
}

# initialise the system 

def init(): 
    print("Welcome to Bank of India.")
    print("""
1. Existing customer enter '1' to login.
2. New customer enter '2' to create an account. 
    """)

    haveAccount = int(input("----> "))
    
    if haveAccount == 1:

        login()
    elif haveAccount == 2:

        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("""
                    *******LOGIN******          
    """)
    print("*********",currentTime,"********")
    accountNumberFromUser = int(input("What is your account number? \n--->"))
    password = input("What is your password? \n--->")
    print("\n")
    for accountNumber, userDetails in database.items(): # authethication 
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)
    
    print("*******=========================********")
    print("Invalid Account Number or Password Entered, Try Again")
    login()

    


def register():  # register func
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password] # returns information of the user to the main database

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaint (4)Logout (5) Exit \n---> ")) # collect information to perform bank operation

    if (selectedOption == 1):

        deposit()
    elif (selectedOption == 2):

        withdrawal()
    elif (selectedOption == 3):
        
        customerReport()
    elif (selectedOption == 4):

        logout()
    elif (selectedOption == 5):
        print("Transaction is now complete")
        print("Thank you for choosing 'Bank of India' as your prestigous bank")
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

# customer report

def customerReport():
    print("What issue will you like to report")
    messageComplaint = input("Enter your complaint \n--> ")
    print("\n")
    if (len(messageComplaint) > 0 ):
        print("Thank you for your complain, We will get back to you as soon as possible.")
        print("\n")
        operationAgain()
    else:
         print("Enter a valid message")
         customerReport()

# deposit function

def deposit():
    moneyDeposit = int(input("How much would you like to deposit---> "))
    if (moneyDeposit > 10):
        newBalance = userBalance + moneyDeposit
        print("This is your current balance --> %d" % newBalance)
        print("Transaction Id--> %d" % random.randint(100000, 1000000001))
        print("\n")
        operationAgain()
    else:
        print("Please try again")
        deposit()

# withdrawal function

def withdrawal():
    withdraw_Amount = int(input("Enter the amount to withdraw--> "))
    if (withdraw_Amount >= 1000 and withdraw_Amount < userBalance ):
        newBalance = userBalance - withdraw_Amount
        print("\n")
        print("Take your cash --> %d" % withdraw_Amount)
        print("Transaction Id--> %d" % random.randint(100000, 1000000001))
        print("\n")
        operationAgain()
    else:
        print("Please try again")
        withdrawal()

# performs bank operation again after use is done with bank operation

def operationAgain():
    print("will you like to perform another transaction or logout.")
    selectedChoice = int(input("Enetr 1 to continue\nEnter 2 to logout\n----> "))
    if (selectedChoice == 1):
        print('''
        Welcome Back, what would you like to do.
        (1). deposit
        (2). Withdrawal
        (3). Complaint
        (4). Exit
        ''')
        newTrans = int(input("---->  "))
        if (newTrans == 1):
            deposit()
        if (newTrans == 2):
            withdrawal()
        if (newTrans == 3):
            customerReport()
        if (newTrans == 4):
            exit()

# generate bank accoubt for user

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

# logout the user from the system

def logout():
    login()

init()
