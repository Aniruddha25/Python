a=[4,7,8]
b=[4,8,7]
#Minimum and maximum element from list
print(max(a))
print(min(b))
#Converting tuple into list
b=list((3,5,7))
print(type(b))
#For removing all element from list
b.clear()
print(b)
#copying the string
c=a.copy()
print(c)
#for adding list inside another list

c.extend(a)#we can use append also
c.sort()#sorting the list
c.reverse()#reversing the list
c.pop()#for removing last element from list
c.insert(5,10)#position and value are the parameters
print(c)
#frequency of element
print(c.count(4))
#for traversing the list
for i in a:
    print(i, end =' ' )

#sum of elements of list
print(sum(a))
#list comprehenssions
l=[ word for word in "Aniruddha"]
l="".join(l)
print(l)
#Collection module
from collections import deque
#The Python deque() is a double-ended queue which allows us to add and remove elements from both the ends.
t=[4,5,6,7,8]
t=deque(t)
t.appendleft(3)
t.pop()
print(t)
