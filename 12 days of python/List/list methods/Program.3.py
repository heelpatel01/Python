#find out minimum and maximum value from a list 

List =[3,2,7,6,10,5,1,12]
min=List[0]
max=List[0]
for i in List:
    if i<=min:
        min=i
    if i>=max:
        max=i
        
print("Minimu Number Of List Is",min)
print("Minimu Number Of List Is",max)   