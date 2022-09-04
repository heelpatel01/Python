# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# -------------------------------------------

#if statement
if(5>2): #we need to write colon(:) bcz By Watching Symbol of Colon Compiler can understand that They have to Enter in this line (line mai gus ne ke liye use hota hai ye symbol)
 print("5 is greater than 2") #there is required indent( ) means whitespace before wrinting statemrnt.otherwise it will Throw you error IndentationError.

 #----------------------------------------------------------------------------

# if else statemrnt

print('enter your age')
age = int (input()) #syntex.- variable name = datatype(input()) note/-Must Use Perfect Spacing. for run program without any error.

if age>18:
    print("you can drive vhicle")
if age>110:
    print("you are overaged so go on your bad do rest")
if age<4:
    print("you are kid 😊you should not use mobile even 😡")
elif age<18:
    print("you can't drive vhical")
else:
    print('''Come At Office We Will Decide "you can drive or not"''')#here.we can use triple,four apostrophe(''') for identifying which text have to print.