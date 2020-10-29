
#-------------Problem 4-------------------
def ProdSum():
    userInput = 1
    productTotal = 1
    sumTotal = 0
    inputHistorySum = []
    inputHistoryProduct = []
    upperBounds = 99
    lowerBounds = 0
    breakNumber = 25
    while userInput:
        userInput = int(input("Input a number from 1-99\tInput 0 to End\t\t"))
        if userInput > upperBounds or userInput < lowerBounds:
            while userInput > upperBounds or userInput < lowerBounds:
                userInput = int(input("INVALID INPUT:\nInput a number from 1-99\tInput 0 to End\t\t"))                    
        if userInput <= breakNumber and userInput != lowerBounds:
            productTotal *= userInput
            inputHistoryProduct.append(userInput)            
        if userInput > breakNumber and userInput <= upperBounds:
            sumTotal += userInput
            inputHistorySum.append(userInput)            
        if userInput == lowerBounds:
            print("\n\n\n\t\tThe Product of the numbers " + str(inputHistoryProduct) + " is: %d\n\t\tThe Sum of the numbers " % productTotal + str(inputHistorySum) + " is: " + str(sumTotal) + "\n\n\n")
ProdSum()

# ------------Problem 3-------------------
def simpleEncryption():
    encryptString = input(
        "Enter alphanumeric characters (a thru z and 0 thru 9), e.g. no spaces or special characters\n").lower()
    print(encryptString)
    encryption = []
    for x in encryptString:
        if x.isalpha():
            if 10 > ord(x) - 96:
                encryption.append(str("0" + str(ord(x) - 96)))
            else:
                encryption.append(str(ord(x) - 96))
        if x.isdigit():
            encryption.append(str("0" + x))
    encryptedString = ""
    encryptedString = encryption[0:len(encryption)]
    print(str(encryptedString).replace('\'', "").replace(',', "").replace(" ", "").replace("[", "").replace("]", ""))

simpleEncryption()


#-----------------Problem 2------------------
def newDict():
    numOfInputs = int(input("How many Inputs do you want for your dictionary?\t"))
    keyList = []
    valueList = []
    while numOfInputs > 0:
        val = input("Please Enter a Key:\t")
        keyList.append(val)
        val = input("Please Enter a Value:\t")
        valueList.append(val)
        numOfInputs -= 1    
    valSpot = 0    
    newList = []
    zipObj = zip(keyList, valueList)
    newdiction = dict(zipObj)            
    print("YOUR DICTIONARY IS:\n" , newdiction)    
newDict()


#Problem 1------------------
def Splitter():
    strInput = input("Enter a Word or Sentence for the Splitter:")
    vowels = ['a','e','i','o','u']
    vowelBuffer = []
    consonantBuffer = []
    for x in strInput:
        if x in vowels:
           vowelBuffer.append(x)       
        else: consonantBuffer.append(x)
    print("\""+ ''.join(consonantBuffer) + ''.join(vowelBuffer) + "\"")

Splitter()
