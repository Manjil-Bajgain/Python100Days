class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"The  ${amount} is deposited. New balance is ${self.balance}")

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficent balance:")
        else:
            self.balance-=amount
            print(f"${amount} is withdraw.New balance is ${self.balance}")

    def display(self):
        print(f"Name is {self.name}.\n Balance is {self.balance}")

#creating an account with user input
name=input("Enter the account holder name:")
initial_balance=float(input("Enter the initial balance to that account:"))

#creting an object
account=BankAccount(name,initial_balance)


while True:
    print("Slect the operation:")
    print("1.Deposit")
    print("2.Withdarw")
    print("3.Display")
    print("4.Exit")
    

    choice=input("Enter your choice(1-4)").strip()
    
    if choice=="1":
        amount=float(input("Enter the amount ot deposit:"))
        account.deposit(amount)
    
    elif choice=="2":
        amount=float(input("Enter the amount to withdraw:"))
        account.withdraw(amount)

    elif choice=="3":
        account.display()
        break
    else:
        print("Invalid input!!!")
        break

        
