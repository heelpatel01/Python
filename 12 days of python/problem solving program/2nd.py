'''Calculate the Total Mark , Avg. Mark and Grade of a Student'''

subject1=int(input("Enter subject1 marks"))
subject2=int(input("Enter subject2 marks"))
subject3=int(input("Enter subject3 marks"))
subject4=int(input("Enter subject4 marks"))
subject5=int(input("Enter subject5 marks"))

Total_Marks=subject1+subject2+subject3+subject4+subject5

average_markes=Total_Marks/5

print(average_markes)

if average_markes>=90:
 print("GrandMaster")
elif average_markes>=80 and average_markes<=89:
 print("Heroik")
elif average_markes>=70 and average_markes<=79:
 print("Dimond")
elif average_markes>=60 and average_markes<=69:
 print("Platinum")
elif average_markes>=50 and average_markes<=59:
 print("Gold")
elif average_markes>=40 and average_markes<=49:
 print("Silver")
else:
 print("Fail!...Bettar luck for next time")