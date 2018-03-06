#string cheatsheet

#str.find()
#use when the index of the substrinis needed 
string = "catch my catatonic cat"
subString = "cat"
stringIndex = string.find(subString)
print(stringIndex)


#'in' operator
#'in' will return a boolean, says weather the sub appears or not
if(subString in string):
    print("yes")
else:
    print("no")


#str.lower
#converts a string into lowercase to make
#comparisons ignoring caps

crazyString = "I will be easy to cAtch mt cAtAtonic cAt."
stringIndex = crazyString.lower().find(subString)
print(stringIndex)
stringIndex = crazyString.lower().find(subString)
print(stringIndex)


#str.lowet() doesnt change str.
#the first print statement changes all caps to non caps
#the second print statement prints the original crazyString

print(crazyString.lower())
print(crazyString)

#comparison operator
if crazyString > string:
    print("crazy")
else:
    print("lower is greater than uppercase")

if "z" < "a":
    print("uppercase letters come first")

#str.find() [optional parameters]

stringIndex = string.find(subString, 19)
print(stringIndex)

#str.split() the number in brackets is the list index it will display.

someValues = "Laconia Gilford Belmont"
listOfValues = someValues.split()
print(listOfValues[1])
print(listOfValues[2])


keyValuePairs = "Bill: Laconia, Jane: Gilford , Tom: Belmont"
listOfPairs = keyValuePairs.split(", ")
count = 0
while count < len(listOfPairs):
    fname, town = listOfPairs[count].split(": ")
    print("first name is: " + fname + "\n town is: " + town)
    count += 1
    
