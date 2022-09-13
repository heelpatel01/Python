'''
Reverse list using positive index and nagative index.
l=[10,20,30,40,50]
what we want:-
50
40
30
20
10
'''
#its for positive index.
'''
l=[10,20,30,40,50] 
i=len(l)-1
while 0<=i:
    print(l[i])
    i=i-1
'''
#irs for negative index.

#not smart way 👇🏼(done By me)
'''
l=[10,20,30,40,50] 
i=-len(l)+4
while i>=-5:
    print(l[i])
    i=i-1
'''

#smart way
l=[10,20,30,40,50]
i=-1
while i>=-5: #or u can say i>=(-len(l))
    print(l[i])
    i=i-1