'''
WAP TO DISPLAY MULTIPICATION TABLE OF 5.
5*1
5*2
5*3
5*4
5*5
5*6
5*7
5*8
5*9
5*10

start from 1 
stop 10
'''

#❌ i=5  #i value 5
# num=1 #num which is by default5
# while num<=10:  #jab tak num 10 ke barabar nahi ho jata tab tak niche vli condition chlegi
#  i=num*i      #5*1=5 5 is stored un num
#  num=num*i      #5+1=6  6 will store in num
#  print(num)
 
#    #it will print 6, than againcheck  ❌
 
num=int(input("Enter Number Which You Want To get tables"))
i=1
while i<=10:
    print(num,'*',i,'=',num*i)
    i=i+1