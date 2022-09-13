'''--------9.sort()--------'''
'''
It is  used for sorting or arranging elements either in ascending or descending order.
'''


l=[10,2,6,3,7,5,4,1,8,9]
l.sort() #by default it will arrange in ascending order
print(l)
l.sort(reverse=True) #For printing Descending order
print(l)

#------Continue------#

'''
NOTE: If list contain Numbers Thenit eill work based on acsending order , but if the list contain String then it will work in Alphabet order(Just Like Dictionary)
'''
name=["Heel","Dipendra","Avadh","Dixit","Jay","shlok","darsh","Bhavik"]
name.sort()
print(name)

#------Continue------#

'''
NOTE:If list contain heterogenous elements then in this case sort() will not work.
'''

# l=['heel','dipendra',1,2]
# l.sort()
# print(l) 
#TypeError Will Come