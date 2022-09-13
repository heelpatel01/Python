'''
l=['heel','dipendra','deep','avadh']
Expected Output:-
New_list=['hl','da','dp','ah']

'''
l=['heel','dipendra','deep','avadh']
New_l=[]
for i in l:
    pt=len(i)-1
    New=i[0]+i[pt]
    New_l.append(New)
print(New_l)
   
    
