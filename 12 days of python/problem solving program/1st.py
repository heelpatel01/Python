# '''A company decides to give bonus to its employee on this Diwali.
# A '5%' bonus on salary is given to the male workers and '10%' bonus salary to the female workers.
# If the salary of the emaployee is less than 15000 then the employee get an extra '3%' bonus on the salary
# WAP to enter your salary and gender then calculate the bonus that has to given to the employee and display the salary that the employee will get.'''

gender=input("Gender:- ")
salary = int(input("enter your slary:- "))

if gender=='Male':
    bonus=salary*0.05
else: 
    bonus=salary*0.10

if salary<15000:
    totalsalary=salary*0.03+bonus

totalsalary=totalsalary+bonus

# salary=bonus+salary
print(totalsalary)

'''
sal=int(input("Enter Your Salary"))
Gen=input("Male/Female:-")

if Gen=='male':
    bonus=sal*0.05
else:
    bonus=sal*0.10

if sal<10000:
    bonus=sal*0.03+bonus
bonus=bonus+sal
print(bonus)
'''