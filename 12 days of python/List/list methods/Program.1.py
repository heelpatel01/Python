''' Wap to check weather your luckey number is present inside list or not'''

#method 1.
'''
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13]
luckey=int(input("Enter Your Luckey Number"))
print(luckey in numbers)
'''
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13]
choice=int(input("Enter Your Luckey Number: "))
if choice in numbers:
    print("yes your luckey number is available in list")
else:
    print("no there is not available ypur luckey number")