#descending order by price.
items=[("Burger",500), ("Pizza",2150), ("Fries",400)]
items.sort(key=lambda x: x[1], reverse=True)
print(items)
'''
output:
[('Pizza', 2150), ('Burger', 500), ('Fries', 400)]
'''

#Remove
lst = [(), (9, 4), (), (3,)]
lst = [x for x in lst if x]
print(lst)
'''
output:
[(9, 4), (3,)]
'''

#Modify
t = (1, 2, 3)
l = list(t)
l[1] = 99
t = tuple(l)
print(t)
'''
output:
(1, 99, 3)
'''

#Delete
t = (1,2,3,4)
l = list(t)
del l[3]
t = tuple(l)
print(t)

'''
output:
(1, 2, 3)
'''
