#~~~~~~~~~~~~~~~Problem 2~~~~~~~~~~~~~~~~~~~~~~~~~
class Person:
    name = ""
    age = ""
    gender = ""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Employee(Person):
    title = ""
    salary = ""
    def __init__(self, name, age, gender, title, salary):
        super().__init__(name,age,gender)
        self.title = title
        self.salary = salary
    def identifyYourself(self):
        print("\n\n\t" + self.name + "'s info is: Name is " + self.name + ", Age is " \
            + self.age + ", Gender is " + self.gender + ", Title is " \
            + self.title + ", and Salary is " + self.salary)

George = Employee("George", "30", "Male", "Manager", "50000")
George.identifyYourself()

print("\n")
#~~~~~~~~~~~~~~~Problem 1~~~~~~~~~~~~~~~~~~~~~~~~~
class Car:	
    condition = "new"    
    mpg = ""
    model = ""
    color = ""
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("Corvette" , "Black" , "30")
print(my_car.model)
print(my_car.color)
print(my_car.mpg)
print(my_car.condition)