#~~~~~~~~~~~~~~~Problem 2~~~~~~~~~~~~~~~~~~~~~~~~~
class Person:
    name = ""
    dateOfBirth = ""
    placeOfBirth = ""
    sex = ""
    def __init__(self,name,dateOfBirth,placeOfBirth,sex):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.placeOfBirth = placeOfBirth
        self.sex = sex
    def identifyPerson(self):
        print("Name: " + self.name + "\nDate of Birth: " + self.dateOfBirth + "\nPlace of Birth: " + self.placeOfBirth + "\nSex: " + self.sex)

class Employee():
    dateOfHire = ""
    Department = ""
    jobTitle = ""
    def __init__(self, dateOfHire,Department,jobTitle):        
        self.dateOfHire = dateOfHire
        self.Department = Department
        self.jobTitle = jobTitle
    def identifyYourself(self):
        print("Date of Hire: " + self.dateOfHire + "\nDepartment: " + self.Department + "\nJob Title: " + self.jobTitle)

class Salaried(Person,Employee):
    taxBracket = ""
    salary = ""
    def __init__(self,name,dateOfBirth,placeOfBirth,sex,dateOfHire,Department,jobTitle,salary,taxBracket):
        Person.__init__(self,name,dateOfBirth,placeOfBirth,sex)            
        Employee.__init__(self,dateOfHire,Department,jobTitle)            
        self.taxBracket = taxBracket
        self.salary = salary
    def whoAreYou(self):
        print("Name:\t\t\t"+self.name+"\nDate of Birth:\t\t"+self.dateOfBirth+"\nPlace of Birth:\t\t"+self.placeOfBirth+"\nSex:\t\t\t"+self.sex+"\nDate of Hire:\t\t"+self.dateOfHire+"\nDepartment:\t\t"+self.Department+"\nJob Title:\t\t"+self.jobTitle+"\nSalary:\t\t\t"+self.salary+"\nTax Bracket:\t\t"+self.taxBracket)

christopherWelch = Salaried("Christopher Welch", "January 1, 1980", "New York, NY", "Male", "May 1, 2005", "Finance", "Manager", "100,000", "29%")        
christopherWelch.whoAreYou()

'''
#~~~~~~~~~~~~~~~Problem 1~~~~~~~~~~~~~~~~~~~~~~~~~
class Car:	
    condition = "new"    
    mpg = ""
    model = ""
    color = ""
    tankSize = 0
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def getSpecs(self):
        print("MODEL: " + self.model)
        print("COLOR: " + self.color)
        print("MPG: " + self.mpg)
    def setSpecs(self, model,color,mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def milesDriven(self,tankSize):
        tanksDriven = float(input("\nHow many times have you had to fill the Tank?: "))
        print("With a Tank Size of: " + str(float(tankSize)) + " Gallons,")
        print("You have driven: " + str( tanksDriven * tankSize * float(self.mpg) ) + " Miles\n\n")

class mySportsCar(Car):
    def __init__(self,model,color,mpg):
        super().__init__(model,color,mpg)

my_car = Car("Corvette" , "Black" , "30")
my_car.setSpecs("370z","White","45")
my_car.getSpecs()
my_car.milesDriven(15)
newFastCar = mySportsCar("Ferrari","Red","12.3")
newFastCar.getSpecs()
'''