# -*- coding: utf-8 -*-
# lesson01_hm
# Time: Sat Oct 31 16:06:58 2015
# author: Hongyang

bread = raw_input("How many bread do you have?")
peanutbutter = raw_input("How many peanut butter do you have?")
jelly = raw_input("How many jelly do you have?")

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
if bread >= 2 and peanutbutter >= 1 and jelly >= 1 :
    print "You can enjoy peanut butter and jelly sandwich!"
else: print "I am sorry, not enough materials for making a peanutbutter and jelly sanwich!"
# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
x = int(bread)/2
y = int(peanutbutter)
z = int(jelly)
num = min(x, y, z)
if bread >= 2 and peanutbutter >= 1 and jelly >= 1 :
        print "You can enjoy {0} peanut butter and jelly sandwich!".format(num)
else: print "I am sorry, not enough materials for making a peanutbutter and jelly sanwich!"
# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
bread = raw_input("How many bread do you have?")
peanutbutter = raw_input("How many peanut butter do you have?")
jelly = raw_input("How many jelly do you have?")
x = int(bread)
y = int(peanutbutter)
z = int(jelly)
flag = min (x/2, y, z)

if bread >= 2 and peanutbutter >= 1 and jelly >= 1:
    if x%2 == 1:
        if flag == x/2 and max(y,z) > flag:
            print "You can enjoy {0} peanut butter and jelly sanwich, and 1 open faced sanwich".format(flag)
        elif flag < x/2 and max(y-flag, z-flag)> 1:
            print "You can enjoy {0} peanut butter and jelly sanwich, and {1} open faced sanwich".format(flag, min(x-2*flag,max(y-flag, z-flag)))
    else : print "You can enjoy {0} peanut butter and jelly sandwich!".format(flag)
else: print "I am sorry, not enough materials for making a peanutbutter and jelly sanwich!"

# SKIP or just conceptualize / do part if you want, #4 is pretty tedious...
# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
bread = raw_input("How many bread do you have?")
peanutbutter = raw_input("How many peanut butter do you have?")
jelly = raw_input("How many jelly do you have?")
x = int(bread)
y = int(peanutbutter)
z = int(jelly)
flag = min (x/2.0, y, z)
maxnum = max (x/2.0, y, z)
if bread >= 2 and peanutbutter >= 1 and jelly >= 1:
    print "You can make {0} peanut butter and jelly sandwiches with your materials!".format(flag)
    if x/2.0 == y == z :
        print "And You don\'t need anything more."
    elif x/2.0 == maxnum and x%2 == 0:
        print "And you\'re missing {0} more peanut butter, and {1} more jelly to make {2} more sanwiches.".format(x/2-y, x/2-z, (maxnum-flag))
    elif x/2.0 == maxnum and x%2 == 1:
        print "And you\'re missing {0} more bread, {1) more peanut butter and {2} more jelly to make {3} more sanwiches.".format(1, x/2+1-y, x/2+1-z, (maxinum-flag))
    elif y == maxnum:
        print "And you\'re missing {0} more bread, {1} more jelly to make {2} more sanwiches.".format(2*y-x, y-z, (maxnum-flag))
    elif z == maxnum:
        print "And you\'re missing {0} more bread, {1} more peanut butter to make {2} more sanwiches.".format(2*z-x, z-y, (maxnum-flag))
else: print "I am sorry, not enough materials for making a peanutbutter and jelly sanwich!"

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich
# but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.


bread = raw_input("How many bread do you have?")
peanutbutter = raw_input("How many peanut butter do you have?")
jelly = raw_input("How many jelly do you have?")
x = int(bread)
y = int(peanutbutter)
z = int(jelly)
flag = min (x/2, y, z)
if bread >= 2 and peanutbutter >= 1 and jelly >= 1:
    print "You can make {0} peanut butter and jelly sandwiches with your materials!".format(flag)
    if x/2 > flag and y > z:
        print "And you can make {0} peanut sandwich.".format(min(x-2*flag, y-flag))
    elif x/2 > flag and y < z:
        print "And you can make {0} jelly sandwiches.".format(min(x-2*flag, z-flag))
                   
else: print "I am sorry, not enough materials for making a peanutbutter and jelly sanwich!"



