'''
Create A New List From A List
------------------------------
------------------------------
------------------------------
l=['hi','hello']
s=['deep','dipu','darsh','param']

expected output 
---------------

['hi Deep', 'hi Dipu', 'hi darsh' , 'hi param', 'hello deep', 'hello darsh', 'hello param']
'''

l=['hi','hello']
s=['deep','dipu','darsh','param']
empty_list=[]
for i in l:
    for j in s:
        empty_list.append(i+' '+j)
print(empty_list)