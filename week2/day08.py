# # Project — Bank Account System

# # 1. Deposit
# # 2. Withdraw
# # 3. Check Balance
# # 4. Transaction History
# # 5. Exit

# class BankAccount:
#     def __init__(self, account_number, account_holder):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = 0 
#         self.transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transaction_history.append(f"Deposited: ${amount}")
    
#     def withdraw(self, amount):
        
#         if amount > 0 and amount <= self.balance:
#                 self.balance -= amount
#                 self.transaction_history.append(f"Withdrew: ${amount}")
#         else:
#                 raise ValueError("Insufficient funds or invalid amount.")
    
#     def check_balance(self):
#         return self.balance
    
#     def get_transaction_history(self):
#         return self.transaction_history
    


    
# account = BankAccount("123456789", "John Doe")
# while True:
#         print("\n1. Deposit")
#         print("2. Withdraw")
#         print("3. Check Balance")
#         print("4. Transaction History")
#         print("5. Exit")
#         choice = input("Choose an option: ")

#         if choice == '1':
#             amount = float(input("Enter amount to deposit: "))
#             account.deposit(amount)
#             print("Account Balance:", account.check_balance())
#         elif choice == '2':
#             try:
#                 amount = float(input("Enter amount to withdraw: "))
#                 account.withdraw(amount)
#                 print("Account Balance:", account.check_balance())
#             except ValueError as e:
#                 print("Error:", e)
#         elif choice == '3':
#             print("Current Balance:", account.check_balance())
#         elif choice == '4':
#             print("Transaction History:")
#             for transaction in account.get_transaction_history():
#                 print(transaction)
#         elif choice == '5':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid option. Please choose again.")

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
        else:
            raise ValueError("Invalid deposit amount.")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
        else:
            raise ValueError("Insufficient funds or invalid amount.")
    
    def check_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    
account = BankAccount("123456789", "John Doe")
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        try:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Account Balance:", account.check_balance())
        except ValueError as e:
            print("Error:", e)
    elif choice == '2':
        try:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            print("Account Balance:", account.check_balance())
        except ValueError as e:
            print("Error:", e)
    elif choice == '3':
        print("Current Balance:", account.check_balance())
    elif choice == '4':
        print("Transaction History:")
        for transaction in account.get_transaction_history():
            print(transaction)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose again.")
