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