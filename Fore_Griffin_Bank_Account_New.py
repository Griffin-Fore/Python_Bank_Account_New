# The BankAccount class should have a balance. BREAK
# When a new BankAccount instance is created, if an amount is given,
# the balance of the account should initially be set to that amount; 
# otherwise, the balance should start at $0. BREAK
# he account should also have an interest rate in decimal format. BREAK
# The interest rate should be provided upon instantiation BREAK
class BankAccount:
    # Use a classmethod to print all instances of a Bank Account's info
    all_accounts = []

    def __init__(self, balance = 100, interest_rate = 0.05):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print(f"Depositting {amount}")
        self.balance += amount
        print(f"Balance: {self.balance}")

        return self

    def withdraw(self, amount):
        if(amount <= self.balance):
            print(f"Current Balance: {self.balance}.")
            print(f"Withdrawing {amount}.")
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print(f"Attempting to withdraw {amount} from {self.balance}")
            print("Insufficient funds: Charging a $5 fee ")
            self.balance -= 5
            print(f"Balance after fee: {self.balance}")

        return self
    
    def display_account_info(self):
        print("Displaying account info")
        print(f"Account balance: {self.balance}")
        print(f"Account interest rate: {self.interest_rate}")

        return self

    def yield_interest(self):
        print("Yielding interest")
        print(f"Interest rate: {self.interest_rate}, Current balance: {self.balance}")
        self.balance *= (1 + self.interest_rate)
        print(f"New balance: {self.balance}")

        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.balance)
            print(account.interest_rate)



Account_1 = BankAccount()
Account_1.display_account_info()
Account_1.deposit(60).deposit(70).withdraw(40).yield_interest().display_account_info()
Account_1.display_account_info()

Account_2 = BankAccount(150, 0.06)
Account_2.display_account_info().deposit(50).deposit(50).withdraw(30).withdraw(30).withdraw(30).withdraw(30).yield_interest().display_account_info()

BankAccount.print_all_accounts()