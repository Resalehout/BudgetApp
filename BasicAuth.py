import random 
import datetime

database = {}

def init():

    print(datetime.datetime.now())
    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have an account with us? 1(yes) 2(no): "))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print("You have selected an invalid option")
        init()


def login():
    selectedOption = int(input("Do you want to log in to your account? (1) Yes (2) No(to exit): "))
    if selectedOption == 1:
        userAccountNumber = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        
        for accountNumber, userDetails in database.items():
            if accountNumber == userAccountNumber:
                if userDetails[3] == password:
                    print(f"Welcome {userDetails[0]} {userDetails[1]}")
                    bankOperations(userDetails)
                else:
                    print("Invalid account number or password")
                    login()
            else:
                print("Invalid account number or password")
                login()

    elif selectedOption == 2:
        exit()
    else:
        print("Invalid option selected")

        login()


def register():
    print("Account Registration...")

    email = input("Enter email address: \n")
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    password = input("Create a password: \n")
    balance = generateBalance()

    accountNumber = generateAccountNumber()
    
    database.update({accountNumber: [first_name, last_name, email, password, balance] })

    print("Your account has been created")
    print("=============================")
    print("Your account number is: %d" % accountNumber)
    print("Make sure to keep it safe")
    print("=============================")

    login()

def bankOperations(user):
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Inquiry (4) Logout (5) Exit: "))
    if selectedOption == 1:
        depositOperation(user)
    elif selectedOption == 2:
        withdrawalOperation(user)
    elif selectedOption == 3:
        inquiry(user)
    elif selectedOption == 4:
        logout()
    elif selectedOption == 5:
        exit()
    else: 
        print("Invalid option selected")
        bankOperations(user)

def depositOperation(user):
    print("***Deposit Operation***")
    deposit = int(input("Enter amount: "))
    user[4] = user[4] + deposit 
    print("Operation Successful")
    bankOperations(user)


def withdrawalOperation(user):
    cash = int(input("Enter ammount: "))
    if cash >= user[4] or cash == user[4]:
        print("Insufficient balance")
        bankOperations(user)
    else: 
        user[4] = user[4] - cash
        print("Take your cash")  
        bankOperations(user)


def inquiry(user):
    selectedInquiry = int(input("What would you like to do? (1) Check Balance (2) Complaint: "))
    if selectedInquiry == 1:
        print(f"Your current balance is ${user[4]}")
        bankOperations(user)
    elif selectedInquiry == 2:
        complaint = input("What is your complaint? ")
        print("Thank you for contacting us")
        bankOperations(user)
    else:
        print("You selected an invalid option, try again...")
        inquiry()

def logout():
    print("***Logging out***")
    login()

def exit():
    print("Have a nice day.")


def generateAccountNumber():
    
    return random.randrange(1111111111,9999999999)

def generateBalance():

    return random.randrange(1000,1000000)


init()

