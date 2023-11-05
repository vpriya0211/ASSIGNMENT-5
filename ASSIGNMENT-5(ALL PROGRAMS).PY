# Challenge 1: Square Numbers and Return Their Sum
#Implement a class Point that has three properties and a method.
#Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z. 
#Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

point_instance = Point(1, 3, 5)
result = point_instance.sqSum()
print(result)

# Challenge 2: Implement a Calculator Class
#Task 1👉:Implement an initializer to initialize the values of num1 and num2. Properties num1 & num2
#Task 2👉:Methods • add() • subtract() • multiply()• divide()

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero"
        return self.num2 / self.num1

obj = Calculator(10, 94)
print('addition:',obj.add())      
print('subtraction:',obj.subtract()) 
print('multiply:',obj.multiply()) 
print('divide:',obj.divide())

# Challenge 3: Implement the Complete Student Class
#Task👉:Implement the following properties as private:• name • rollNumber 
#    👉:Include the following methods to get and set the private properties above:
#       • getName() • setName() • getRollNumber() • setRollNumber() 
#    👉:Implement this class according to the rules of encapsulation.

class Student:
    def __init__(self, name, rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

student_instance = Student("Priya", "26086")
print("Name:", student_instance.getName())
print("Roll Number:", student_instance.getRollNumber())

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