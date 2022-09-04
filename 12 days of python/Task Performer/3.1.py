#method 2 Smart Method.

number_1 = int(input("enter The First Number:- "))
number_2 = int(input("enter The second Number:- "))
number_3 = int(input("enter The third Number:- "))


if number_1>number_2 and number_1>number_3:
    print(number_1,"is greatest number than",number_2,"and",number_3)
elif number_2>number_1:
    print(number_2,"is greatest")
elif number_3==number_2==number_1:
    print("all numbers are same")
else:
    print(number_3,"is greatest")
