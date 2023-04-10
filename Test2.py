"""Write a program to produce Fibonacci series in Python?"""

def fibonacci(n):
    sequence = [0,1]
    
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

fibonacci_sequence = fibonacci(20)
print(fibonacci_sequence)



"""Create a dictionary using while loop? For example student name and roll number?"""
key = ['a','b','c','d']
values = [1,2,3,4]

my_dict = {}
i = 0
while i < len(key):
    my_dict[key[i]] = values[i]
    i += 1
print(my_dict)


"""
2.Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not... 
"""
list =["Ryan", "Kieran", "Mark", "Dhivakar", "Ramu", "Arul"]
friends = [x for x in list if len(x)==4]
print(friends)


# 1.Find the first python developer from below dictionary using while loop? 


list1 = [
{"firstName": 'Mark', "lastName": 'G.', "country": 'Scotland',"continent": 'Europe', "age": 22, "language": 'JavaScript'},
{"firstName": 'Victoria', "lastName": 'T.', "country": 'Puerto Rico',"continent": 'Americas', "age": 30, "language": 'Python'},
{"firstName": 'Emma', "lastName": 'B.', "country": 'Norway',"continent": 'Europe', "age": 19, "language": 'Clojure'}
]
list2 = [
{ "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
{ "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
]

def python_developer(first,second):
    total_list = first + second
    lang_python = [x for x in total_list if x['language'] == "Python" ]
    return lang_python
print(python_developer(list1,list2))



"""
Write a program yourself and try to cover all the concepts based on your learning?
"""

first_name = "Prakash"
last_name = "Ramu"
Account_number = 32270787
Account_bals = 500



# try:
#     print(1/0)
# except ZerodivisionError:
#     raise ('The number should not be in Zero')

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction = []
      
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        self.transaction.append("Deposited", self.amount)
        

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transaction.append("withdraw", self.amount)
        
        
        
        

class SavingAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.01):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self.transaction.append("Interest", self.amount)
        
        
my_account_details = BankAccount('Prakash',1000)
print(my_account_details.balance)
my_account_details.deposit(500)
print(my_account_details.balance)
my_account_details.withdraw(1000)
print(my_account_details.balance)

my_account_details.add_interest()

