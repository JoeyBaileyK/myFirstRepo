hello = "ABBDCDBCBACDBCDDCBBADCBABCDCDCABABCDBCADACDCBACDBDCABDDCABDCDDDBACDBACDCCB"
tally_a = 0
tally_b = 0
tally_c = 0
tally_d = 0
count = 0
for letter in hello:
    if letter == 'C':
        tally_c +=1
    if letter == 'B':
        tally_b +=1
    if letter == 'A':
        tally_a +=1
    if letter == 'D':
        tally_d +=1
    count += 1
print("total: " + str(count)) 
print("A: " + str(tally_a) + " B: " + str(tally_b) + " C: " + str(tally_c) + " D: " + str(tally_d))
A_percent = tally_a*100//count
B_percent = tally_b*100//count
C_percent = tally_c*100//count
D_percent = tally_d*100//count
print(str(A_percent) + "% is a, " + str(B_percent) + "% is b, " +
      str(C_percent) + "% is c, " + str(D_percent) + "% is d")
