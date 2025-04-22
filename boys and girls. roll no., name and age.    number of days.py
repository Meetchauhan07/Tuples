#find out number of boys and girls in the list.
lst = [("Ram",), "Sita", ("Shyam",), "Gita"]
boys = girls = 0
for x in lst:
    if isinstance(x, tuple):
        boys += 1
    else:
        girls += 1
print("Boys:", boys, "Girls:", girls)
'''
output:
Boys: 2 Girls: 2
'''
#Three lists separately for roll no., name and age
students = [(1, "Amit", 20), (2, "Neha", 21), (3, "Ravi", 22)]
rolls = [s[0] for s in students]
names = [s[1] for s in students]
ages = [s[2] for s in students]
print("Rolls:", rolls)
print("Names:", names)
print("Ages:", ages)
'''
output:
Rolls: [1, 2, 3]
Names: ['Amit', 'Neha', 'Ravi']
Ages: [20, 21, 22]
'''

#Two date tuples and find the number of days between the two dates.
from datetime import date
d1 = (1, 7, 2024)
d2 = (8, 4, 2025)
days = (date(d2[2], d2[1], d2[0]) - date(d1[2], d1[1], d1[0])).days
print("Days between:", days)
'''
output:
Days between: 281
'''





