'''
WAP TO READ THE NUMBERS UNTILL -1 IS NOT  ENTERED. ALSO COUNT THR NEGATIVES, POSITIVES AND ZEROS ENTERED BY THE USER.
'''
#WHILE FOR THE UNTILL -1 JAB TAK -1 ENTER NAHI KAREGA TAB TAK EXIT NAHI MILEGA🙂 ``'

'''
num=int(input("Enter The -1 if you want to exit"))

neg=0
pos=0
Zero=0

while num!=(-1):
    if num>0:
        pos=pos+1
    elif num<0:
        neg=neg+1        
    else:
     Zero=Zero+1
    num=int(input("Enter The -1 if you want to exit"))


print("numners of positive",pos)
print("numners of negative",neg)
print("numners of Zeros",Zero)
'''


# print("POSITIVE NUMBER ENTERED {0} TIMES NEGATIVE NUMBERS ENTERED {1} TIMES ZERO ENTERED {3} TIMES",pos,neg,Zero)
    # print("enter the -1 to exit")

num=int(input("enter -1 to exit program"))

while num!=-1:
    if num>0:
        print("number is positive please enter another number")
    elif num<0:
        print("entered number is negative so please enter -1 if you want to exit")
    else:
        print("entered number is zero so please enter -1 to exit program")
    num=int(input("enter -1 to exit program"))
    