# Challenge 4: Implement a Banking Account
#Task 1:👉 Implement properties as instance variables, and set them to None or 0.
#Account has the following properties:• title • Balance 
#SavingsAccount has the following properties:• interestRate
#Task 2:👉Create an initializer for Account class. 
#The order of parameters should be the following, where Ashish is the title, and 5000 is the account balance:
#Task 3:👉Implement properties as instance variables, and set them to None or 0.
#Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:
#Account("Ashish", 5000, 5)

class Account:
    def __init__(self, title=None, balance=None):
        self.title = title
        self.balance = balance
        
    def __str__(self):
        return f'Account Title: {self.title} and Account Balance: {self.balance}'

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate=None):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def __str__(self):
        return f'Savings Account Title: {self.title} , Savings Account Balance: {self.balance} and Interest rate: {self.interestRate}'
   
account_obj = Account("Ashish", 5000) 
savings_account_obj = SavingsAccount("Ashish", 5000, 5) 
print(account_obj)
print(savings_account_obj)