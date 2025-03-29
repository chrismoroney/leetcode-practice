# Example explained:
# In the BankAccount class, the balance is private (__balance), 
# meaning it cannot be directly accessed or modified from outside the class. 
# Instead, clients must use the provided methods (deposit(), withdraw(), get_balance()), 
# which contain logic to ensure operations are valid (like preventing negative deposits or overdrafts). 
# This protects the integrity of the account balance.

class BankAccount:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.__balance = 0  # Private attribute (denoted by double underscore)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return f"Current balance: ${self.__balance}"

# Create account
account = BankAccount("123456", "John Doe")

# Interact with the account using methods
print(account.deposit(1000))  # Deposited $1000. New balance: $1000
print(account.withdraw(500))  # Withdrew $500. New balance: $500
print(account.get_balance())  # Current balance: $500

# This will not work as expected since __balance is private
# print(account.__balance)  # AttributeError