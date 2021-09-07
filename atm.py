class atm():
    def __init__(self, name, age, accountNumber, balance):
        self.name = name
        self.age = age
        self.accountNumber = accountNumber
        self.balance = balance
        

    def viewAccount(self):
        print()
        print()
        print("Your Details : ")
        print()
        print("Name :",self.name)
        print("Age :",self.age)
        print("Account Number :",self.accountNumber)
        print("Balance :",self.balance)
        print()
        restart = input("Do another action? y/n : ")
        if restart == 'y':
            useATM()
        else:
            input("Goodbye! ")
            quit()

    def deposit(self):
        print()
        print()
        depAmt = int(input("How much money would you like to deposit? : "))
        print("Current Balance :",self.balance)
        self.balance += depAmt
        print("New Balance :",self.balance)
        print()
        restart = input("Do another action? y/n : ")
        if restart == 'y':
            useATM()
        else:
            input("Goodbye! ")
            quit()
    
    def withdraw(self):
        def withd():
            print()
            print()
            withAmt = int(input("How much money would you like to withdraw? : "))
            print("Current Balance :",self.balance)
            if withAmt>self.balance:
                print()
                print("Invalid Amount, not enough money in balance")
                print()
                withd()
            else:
                self.balance-=withAmt
                print("New Balance :",self.balance)
                restart = input("Do another action? y/n : ")
                if restart == 'y':
                    useATM()
                else:
                    input("Goodbye! ")
                    quit()
        withd()
            

def useATM():
    choice = input("Would you like to view details (v), deposit money (d) or withdraw money (w) ? : ").lower()

    if choice == 'v':
        user1.viewAccount()
    elif choice == 'd':
        user1.deposit()
    elif choice == 'w':
        user1.withdraw()
    else:
        useATM()
user1 = atm("John",43,"7890 3465 8998 7863",100000)
print(user1.balance)
useATM()