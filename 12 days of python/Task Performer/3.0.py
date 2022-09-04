#WAP entered 3 numbers which one is greater than .


#method 1.
number_1= int(input("Enter First Number:- "))
number_2= int(input("Enter second Number:- "))
number_3= int(input("Enter third Number:- "))

if number_1>number_2 and number_1>number_3:
    print(number_1,"is greatest number than",number_2,"and",number_3)
elif number_2>number_1 and number_2>number_3:
    print(number_2,"is greatest number than",number_1,"and",number_3)
elif number_3>number_1 and number_3>number_2:
    print(number_3,"is greatest number than",number_1,"and",number_2)
else:
    print("all numbers are same")
#method 2 Smart Method.

if number_1>number_2 and number_1>number_3:
    print(number_1,"is greatest number than",number_2,"and",number_3)
elif number_2>number_1:
    print(number_2,"is greatest")
elif number_3==number_2==number_1:
    print("all numbers are same")
else:
    print(number_3,"is greatest")
