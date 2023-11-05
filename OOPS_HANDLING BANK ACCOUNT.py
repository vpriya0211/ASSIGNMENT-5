# Challenge 5: Handling a Bank Account
#Task 1:👉In the Account class, implement the getBalance() method that returns balance.
#Task 2:👉In the Account class, implement the deposit(amount) method that adds amount to the balance.
# It does not return anything.
#Task 3:👉In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.
#It does not return anything.
#Task 4:👉In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.
class Account:
    def __init__(self, title=None, balance=None):
        self.title = title
        self.balance = balance
      
    def __str__(self):
        return f'Title: {self.title} and Balance: {self.balance}'
         
    def deposit(self,dep_amt):
        self.balance += dep_amt
        self.dep_amt = dep_amt
        print('**Deposit Accepted**')
        print('Deposit amount:', self.dep_amt)
        print('Balance after deposit amount:', self.balance)
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            self.wd_amt = wd_amt
            print('**Withdrawal Accepted**')
            print('Withdrawal amount:', self.wd_amt)
            print('Balance amount after withdrawal:', self.balance)
        else:
            print('**Funds Unavailable**')
            
    def getBalance(self):
        print('Current Balance amount:', self.balance)      

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        I = self.interestRate * (self.balance / 100)
        return f'InterestRate:{I}'

account_obj = Account("Ashish", 2000)
print(account_obj)
account_obj.getBalance()
account_obj.deposit(500)
account_obj.withdraw(500)

account_obj.getBalance()

savings_account = SavingsAccount("Ashish", 2000, 5)
print(savings_account.interestAmount())