'''
Nested While Loop:-
IF  A WHILE LOOP PRESENT INSIDE ANOTHER WHILE LOOP THEN THIS CONCEPT IS CALLED AS NESTED WHILE LOOP.
SYNTEX-->
while expression1:
    while expression2:
        statement(s2)
    statement(s1)
'''


i=1
while i<=3:
    print('   ',i)
    j=1
    while j<=3:
      print(j)
      j=j+1
    i=i+1