#BudgetApp
Database = {}

class Budget():

    def __init__(self, categories, amount):
        self.categories = categories
        self.amount = amount

    def Deposit(amount, catBal):
        catBal = catBal + amount
        return catBal

    def Withdrawal(category, amount, catBal):
        catBal = catBal - amount
        return catBal

    def Balance(database):
        for category, balance in database.items():
            print(f"{category}: {balance}")

    def fundTransfer(database, category1, amount, category2 ):
        database[category1] = database[category1] - amount
        database[category2] = database[category2] + amount

        return database

def init():
    print("**********Welcome to U-Budget**********")
    menu()

def menu():
    try:
        selectedOption = int(input("What would you like to do?\nSelect\n (1) To Create a Budget Category\n (2) To Make a Deposit into a Category\n (3) To Withdraw from a Category\n (4) To Check The Balance of Each Category\n (5) To Transfer Money between Categories\n (6) To Exit\nEnter an Option: "))
    except ValueError:
        print("Select a valid option")
        menu()

    if selectedOption == 1:
        createCategory()
    elif selectedOption == 2:
        deposit()
    elif selectedOption == 3:
        withdraw()
    elif selectedOption == 4:
        balance()
    elif selectedOption == 5:
        transfer()
    elif selectedOption == 6:
        exit()
    else:
        print("You selected an invalid option, please try again")
        menu()
    
def createCategory():

    category = input("Enter a Category name: ") 
    if category in Database:
        print(f"Budget Category {category} already exists")
        return createCategory()
    else:    
        try:
            amount = int(input("Enter amount in Naira: "))
        except ValueError:
            print("Invalid input") 
            return createCategory()
        budget = Budget(category, amount)
        Database[category] = amount
        print(f"Budget category {category} has been created and funded with N{amount}")
        menu()
    
def deposit():
    print("***Deposit Operation***")
    print("Available Categories")
    for key, value in Database.items():
        print(f"{key}: N{value}")
    category = input("Which budget category do you want to fund?\nEnter Category: ")
    if category in Database:
        cash = int(input("Enter amount in Naira: "))
        bal = int(Database[category]) 
        balance = Budget.Deposit(cash, bal)
        Database[category] = balance
        print(f"You funded the category, {category} with N{cash}\nNew Balance\n{category}:{balance} ")
        menu()
    else:
        print(f"{category} isn't a budget category, select an appropriate option")
        deposit()

def withdraw():
    print("***Withdrawal Operation***")
    print("***Available Categories***")
    for key, value in Database.items():
        print(f"{key}:N{value}")
    category = input("Select a category: ")
    if category in Database:
        cash = int(input("Enter amount you wish to withdraw: "))
        if cash < Database[category]:
            bal = Database[category]
            balance = Budget.Withdrawal(category, cash, bal)
            Database[category] = balance
            print(f"You withdrew N{cash}\nNew {category} balance = N{balance}")
            menu()
        else:
            print("Insufficient balance, you cannot withdraw an amount that is higher than your chosen category balance")
            menu()

    
def balance():
    print("***Category Balance***")
    balance = Budget.Balance(Database)
    menu()

def transfer():
    print("***Available Categories and Balance***")
    balance = Budget.Balance(Database)
    category1 = input("Please Enter the Category you wish to transfer from: ")
    if category1 in Database:
        fromCat = int(input(f"Enter the amount you want to transfer from {category1} budget: ")) 
        if fromCat < Database[category1]:
            category2 = input("Enter the category you wish to transfer to: ")
            if category2 in Database:
                bal = Budget.fundTransfer(Database, category1, fromCat, category2)
                print(f"Transfer of N{fromCat} from {category1} budget to {category2} budget was successful")
                print(f"New {category2} budget")
                for key, value in Database.items():
                    print(f"{key}: {value}")
                    menu()
            else:
                print("Enter valid category")
                return transfer()

        else:
            print("Insufficient balance, you cannot withdraw an amount that is higher than your chosen category balance")
            return transfer()
    else:
        print("Enter valid category")
        return transfer()

def exit():
    selectedOption = int(input("Select\n (1) To Exit Application\n (2) To Return to Menu\nEnter an option: "))
    if selectedOption == 1:
        exitOption = int(input("Are you sure you want to exit?\n (1) Yes\n (2) No\nEnter an option: "))
        if exitOption == 1:
            review = int(input("Rate your experience\n(1) Good\n(2) Neutral\n(3) Bad\nEnter an option: "))
            if review == 1:
                print("We're glad you enjoyed your experience")
            elif review == 2 or 3:
                suggestion = input("Please tell us how we can improve: ")
                print("Thank you for your suggestion")
            else:
                print("You selected an invalid option")
                exit()
            print("Goodbye, have a nice day.")
        elif exitOption == 2:
            menu()
        else:
            print("You selected an invalid option, please try again") 
            exit()
    elif selectedOption == 2:
        menu()
    else:
        print("You selected an invalid option, please try again")
        exit()


init()
    

    


