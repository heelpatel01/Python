'''
WAP to display list elements of a list along with positive and negative index.
suppose we have list
l=[10,20,30,40,50]

expected output is:
10 is presented at 0/-5
20 is presented at 1/-4
30 is presented at 2/-3
40 is presented at 3/-2
50 is presented at 1/-4
'''

l=[10,20,30,40,50]
n=len(l)
for i in range(n):
    l[i]
    # print(l[i],"is prsented",i,"/",i-n)
    print("{} is presented {}/{}".format(l[i],i,i-n))
