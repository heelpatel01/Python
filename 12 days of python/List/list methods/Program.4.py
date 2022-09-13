''''
WAP TO SEARCH AN VALUE FROM A LIST THEN DISPLAY ITS INDEX.
IF THE VALUE IS PRESENT MULTIPLE TIMES THEN PRINT ITS ALL INDICIES AND ALSO COUNT THE NUMBER OF TIMES THAT VALUE IS REPEATED IN THE LIST.
'''

l=[10,20,30,40,10,20,30,50]
i=0
count=0
key= int(input('enter the key to search : '))
while i<len(l):
    if key==l[i]:
        count=count+1
        print(f'{key} is presented at {i} index ')
    i=i+1
print(f'{key} is present {count} times ')