'''l=['heel',9998585975,'patel','parul universiry','vadodara']

print(l[:4:])'''
# ---------------------

''' For Use Of Input in List we have use eval() function
syntex- 
list name = eval(input("write what you want to print"))
'''
# l=eval(input("enter name and number"))
# print(l[1])

'''creation of list using list() function:'''
# l=list((1,2,3,4,5,))
# print(l)

'''creation of list using range() function:'''
# l=list(range(1,11)) #it will print 1 to 10
# print(l)

'''NOTE-list can hold any complex datatype like dict,tuple,etc.'''
# l=[25,{'name': "heel"},list(range(10,20,1)),list((0,100,1))]
# print(l)
#{'name': "heel"}:- is a dictionary data type

# -------------------------

'''
List Is Mutable In Nature, Mutable Means Changeable. means based on Requirement  we can modify the list items.
'''
# l=[1,2,3,40,5,6,7,8,9,10] #by mistake i entered40 on 3rd index i want to replace it by 4.
# print("this is old list: ",l)
# l[3]=4
# print("this is Updated list: ",l)

'''slice in list'''
l=[10,20,30,40,50,60,70,80,90,100]
print(l[::])
print(l[2::2])