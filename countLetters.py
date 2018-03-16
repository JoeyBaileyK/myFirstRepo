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
