# Find Out The value of y
'''
1st.y(x,n)=1+x         #where n=1
2nd.y(x,n)=1+x/n       #where n=2
3rd.y(x,n)=(1+(x**n))  #where n=3
4th.y(x,n)=1+n*x
'''
print('''instructions:-
1st.y(x,n)=1+x          if u want to perform this  instruction press n=1
2nd.y(x,n)=1+x/n        if u want to perform this  instruction press n=2
3rd.y(x,n)=(1+(x**n))   if u want to perform this  instruction press n=3
4th.y(x,n)=1+n*x        if u want to perform this  instruction press Anything but not
''')


x=int(input("x= "))
n=int(input("n= "))

# y=1+x
# print("1+x= ")

if n==1:
    print("1+x is ",1+x)
elif n==2:
    print("1+x/n is ",1+(x/n))
elif n==3:
    print("(1+(x**n)) is ",(1+(x**n)))
else:
    print("4y(x,n)=1+n*x",1+n*x)