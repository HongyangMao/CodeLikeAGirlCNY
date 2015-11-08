# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Get ingredients' numbers
bread = int(raw_input("How much bread do you have?"))
peanut_butter = int(raw_input("How much peanut butter do you have?"))
jelly = int(raw_input("How much jelly do you have?"))
flag = min(bread/2, peanut_butter,jelly)

# Identify which ingredient is limited (assume only one ingredient is limited compared with the other two)
if bread/2 == flag:
    limited_ing = 'bread'
elif peanut_butter == flag:
    limited_ing = 'peanut butter'
else:
    limited_ing = 'jelly'

# Make a condition to only trigger the loop when ingredients are enough for at least one sanwich
# Format the output
while bread >=2 and peanut_butter >=1 and jelly >=1:
    for i in range(flag):
        print"Making sanwich #{0})".format(i+1)
        bread=bread-2
        peanut_butter=peanut_butter-1
        jelly=jelly-1
    print 'All done; only have enough {1} for {0} sanwiches.'.format(flag, limited_ing)

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.
# Get ingredients' numbers
bread = int(raw_input("How much bread do you have?"))
peanut_butter = int(raw_input("How much peanut butter do you have?"))
jelly = int(raw_input("How much jelly do you have?"))
flag = min(bread/2, peanut_butter,jelly)
# Identify which ingredient is limited
if bread/2 == flag:
    limited_ing = 'bread'
elif peanut_butter == flag:
    limited_ing = 'peanut butter'
else:
    limited_ing = 'jelly'
# Make a condition to only trigger the loop when ingredients are enough for at least one sanwich
# Format the output
while bread >=2 and peanut_butter >=1 and jelly >=1:
    for i in range(flag):
        print"Making sanwich #{0})".format(i+1)
        if min(bread/2, peanut_butter,jelly) > 1:
            print"I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread/2-1, peanut_butter-1,jelly-1)
        else:
            pass
        bread=bread-2
        peanut_butter=peanut_butter-1
        jelly=jelly-1
    print 'All done; I ran out of {0}.'.format(limited_ing)
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.
