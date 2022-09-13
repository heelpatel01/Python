'''
11.copy()
⚪it is used for shallow copy of a list,here Shallow Copy Means if we made any modification in the new list won't be reflected in the original list.
⚪Both list will pointing to diffrent memory location
'''
l=[55,6,776,54,32]
i=l.copy()  #cloning
print(l)
print(i)

print(id(l))
print(id(i))

i[2]=8 #it is updating element without affecting to l list
print(l)
print(i)

