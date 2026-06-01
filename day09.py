class BankAccount:
    def __init__(self,account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            self.save_transaction(f"Deposited: ${amount}")
            print(f"Account Balance: {self.balance}")
       
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            self.save_transaction(f"Withdrew: ${amount}")
            print(f"Account Balance: {self.balance}")
            # print(f"Withdrew {amount} from {filename}")
        else:
            raise ValueError("Insufficient funds or invalid amount.")
    
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance
    
    def get_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        return self.transaction_history
    
    def save_transaction_history(self, filename):
        with open(filename, "a") as file:
            for transaction in self.transaction_history:
                file.write(transaction + "\n")
        print(f"Transaction history saved to {filename}")



    def load_transaction_history(self, filename):
        try:
            with open(filename, "r") as file:
                self.transaction_history = file.read().splitlines()
            for transaction in self.transaction_history:
                if "Deposited" in transaction:
                    amount = float(transaction.split("$")[1])
                    self.balance += amount
                elif "Withdrew" in transaction:
                    amount = float(transaction.split("$")[1])
                    self.balance -= amount
            print(f"Transaction history loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. No transaction history loaded.")



    def save_transaction(self, transaction):
        with open("transactions.txt", "a") as file:
            file.write(transaction + "\n")


    
account = BankAccount("123456789", "John Doe")
account.load_transaction_history("transactions.txt") 

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Load Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        
    elif choice == '2':
        try:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError as e:
            print("Error:", e)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        account.get_transaction_history()
    elif choice == '5':
        filename = input("Enter filename to load transaction history: ")
        account.load_transaction_history(filename)
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        account.save_transaction(f"Exited the program.")
        break
    else:
        print("Invalid choice. Please try again.")
