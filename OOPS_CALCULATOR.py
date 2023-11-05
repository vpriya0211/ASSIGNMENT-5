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