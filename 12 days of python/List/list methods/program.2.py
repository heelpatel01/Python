'''
WAP to check your luckey number untill your luckey number with list element.
'''
numbers=[10,20,30,40,50,60,70,80,90]
choice=int(input('enter your luckey number '))
while True:
    if choice in numbers:
     print('yes your luckey number is available')
     break
    else:
     print("Sorry Not Available Your luckey number so enter again")
     choice=int(input('enter your luckey number again'))