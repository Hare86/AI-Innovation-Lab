
class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount} to {self.account_holder}'s account.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount} from {self.account_holder}'s account.")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ₹{self.balance}")
        print("-" * 30)


if __name__ == "__main__":
    
    account1 = BankAccount("Ravi Kumar", 5000.0, "Savings")
    account2 = BankAccount("Sneha Reddy", 10000.0, "Current")

    
    account1.display_balance()
    account1.deposit(1500)
    account1.withdraw(2000)
    account1.display_balance()

    
    account2.display_balance()
    account2.withdraw(12000) 
    account2.deposit(3000)
    account2.display_balance()
