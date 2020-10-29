#-----Problem #3--------------# 
def Recurse(beerNum):
    if beerNum == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.\n\n")        
    else:
        print("%d bottles of beer on the wall, %d bottles of beer." % (beerNum, beerNum))
        print("Take one down and pass it around, %d bottles of beer on the wall.\n" % (beerNum - 1))
        beerNum -= 1
        Recurse(beerNum)

beers = 99
Recurse(beers)


#-----Problem #2--------------# 
newdict = { 'A': 0, 'B': 1, 'C':2, 'D':3}
listKeys = []
listVals = []

def Delist(newdict, nListKeys, nListVals):
    for x in newdict.keys():
        nListKeys.append(x)
    for x in newdict.values():
        nListVals.append(x)
    listKeys.sort()
    listVals.sort()
    return nListKeys, nListVals

Delist(newdict, listKeys, listVals)
print(listKeys)
print(listVals)

#-----Problem #1--------------# 
## A-Z = 65-90     # a-z = 97-122
def Reorder():
    stringGetter = input("Enter a String, 20 Characters or less:\t\t")
    while len(stringGetter) > 20:
        stringGetter = input("20 Characters or less! Enter a String:\t\t")
    stringBuffer= []
    orderedString = ''    
    for x in stringGetter:        
        stringBuffer.append(str(ord(x)))    
    buffList = []
    for x in stringBuffer:
        buffList.append(int(x))       
    stringBuffer.sort()
    buffList.sort()
    print(buffList)
    for x in buffList:
        orderedString += (str(' 0x') + str(x))        
    print(orderedString)

Reorder()
