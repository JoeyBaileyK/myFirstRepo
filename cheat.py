#addition+
num1 = 1
num2 = 2
sum = (num1) + (num2)
#subtraction-
#multiplication*
#division/
#rounding division//
def some_Function():
    print("this that")
    print("and something")




some_Function()

name="jim"
def returnGreeting(name):
    greeting = "hello, " + name
    return greeting

print(returnGreeting("bob"))
print(name)

x = 41
#boolean operators
#replace == with > or < for different effects.
if x == 42: #equals
    print("equal to")
    

i = 0
j = 0
while i < 5:
    while j < 5:
        print(j)
        j += 1
    print('/n##########')
    j = 0
    i += 1


h = 0
e = 0
while h < 5:
    while e < 2:
        print("hello", end='')
        e += 1
    print('/n##########')
    e = 0
    h += 1

#a program that searches for a b c and d in the Hello string

hello = "hello, and good day to all of the cats in the cupboard"
tally_a = 0
tally_b = 0
tally_c = 0
tally_d = 0
count = 0
for letter in hello:
    if letter == 'c':
        tally_c +=1
    if letter == 'b':
        tally_b +=1
    if letter == 'a':
        tally_a +=1
    if letter == 'd ':
        tally_d +=1
    count +=1
print("total: " + str(count)) 
print("C: " + str(tally_c) + " G: " + str(tally_b) + " A: " + str(tally_a) + " T: " + str(tally_d))

#makign a list, or array
colors = ["red", "gold", "green"]
#identifying a certain thing within the array, starts at 0
color = colors[1]
print(color)

colors[:3]

favoriteColors = {
    'Graham': 'blue',
    'Eric': 'green',
    'Terry': 'orange'}
color = favoriteColors['Graham']
print(color)
