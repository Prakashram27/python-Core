



"""
Write a program yourself and try to cover all the concepts based on your learning?
"""

Account_holder_name = 'Prakash Ramu'
Pan_card_number = 'COAPP3035F'
IFSC_Code = 101211
amount_for_opening = 1000


try:
    print(1/0)
except ZeroDivisionError:
    raise ('The number should not be in Zero')

class BankAccount:
    def __init__(self, name, balance=0,filename=None):
        self.name = name
        self.balance = balance
        self.transaction = []
        self.filename = filename
        self.last_transaction = ''
        if filename:
            with open(filename, "a") as f:
                f.write(f"Account opened for {name}\n")
    
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        self.last_transaction = ''
        self.last_transaction = f'Deposited {amount} Successfully'
        print(self.last_transaction)
        # self.transaction.append(("Deposited", amount))
        if self.filename:
            with open(self.filename, "a") as f:
                f.write(f"Deposit of {amount} made. Current balance is {self.balance}\n")
        

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.last_transaction = ''
        self.last_transaction = f'Withdrawal {amount} have been Successfully'
        print(self.last_transaction)
        if self.filename:
            with open(self.filename, "a") as f:
                f.write(f"Withdrawal of {amount} made. Current balance is {self.balance}\n")
        # self.transaction.append(("withdraw", amount))
        
class SavingAccount(BankAccount):
    def __init__(self, name, balance=0,filename=None, interest_rate=0.01):
        super().__init__(name, balance,filename)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        # self.transaction.append(("Interest", self.amount))
        

my_account_details = SavingAccount(Account_holder_name,1000,'bank_transaction_det.txt')
print('Opening Bals:', my_account_details.balance)

my_account_details.deposit(500)
print('After Deposit Bals amount:',my_account_details.balance)
my_account_details.withdraw(1000)
print('After withdraw Bals amount:',my_account_details.balance)
my_account_details.add_interest()
print('Interest Rate Bals amount:',my_account_details.balance)

