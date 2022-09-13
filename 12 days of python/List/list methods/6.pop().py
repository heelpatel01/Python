'''---6.pop()---'''
'''
⚪By Default it is used to remove and return the last element of the list.
⚪But if you want to remove any specified element then we have to provide that specified element index.
'''
l=[1,2,3,4,5]
print(l.pop()) #by default it will delet end element of index
print(l)
print(l.pop(2)) #2 is 2nd index
print(l)
# print(l.pop(98)) #IndexError:pop index out of range