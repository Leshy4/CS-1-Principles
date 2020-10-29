'''----------------#Problem 5---------------------'''
colors = ['Red', 'Black', 'White']
cars = ['Chevrolet', 'Ford', 'Cadillac', 'GMC']
for x in colors:
    for y in cars:
        print(x, y)        

'''----------------#Problem 4---------------------'''
FruitInventory = {'Apples' : 7, 'Bananas' : 10, 'Pears' : 3, 'Peaches' : 2}
FruitPerUnitPrice = {'Apples' : 1, 'Bananas' : 2, 'Pears' : 3, 'Peaches' : 4}
totalNet = 0
for x in FruitInventory:
    totalNet += FruitInventory[x] * FruitPerUnitPrice[x]
print("Total Money Made By Selling all the Fruit is: $%d" % totalNet)


'''----------------#Problem 3---------------------'''
isDigit = 0
isLetter = 0
InStr = input("Please enter a string of any length and hit ENTER: ")
for x in InStr:
    if x.isalpha():
        isLetter += 1
    if x.isdigit():
        isDigit += 1
print("Digits = ", isDigit)
print("Letters = %d" % isLetter)

'''----------------#Problem 2----------------------------------------------------------'''
Tom = 24
ageCentury = 100
year = 2019
print("Tom will be %d in " % ageCentury, ageCentury - Tom + year)

'''----------------#Problem 1-------------------------------------'''
numList = [58,98,82,69,90,74,68,88,71,44]
numList.sort()

for x in numList:
    if x < 60:
        x = 'F'
        print("Your grade is: ", x)
    elif x < 70 and x > 59:
        x = 'D'
        print("Your grade is: ", x)
    elif x < 80 and x > 69:
        x = 'C'
        print("Your grade is: ", x)
    elif x < 90 and x > 79:
        x = 'B'
        print("Your grade is: ", x)
    elif x > 89:
        x = 'A'
        print("Your grade is: ", x)