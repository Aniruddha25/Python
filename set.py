a={5,6,7,9,5}#Duplicate value is not added inside set
a.add(4)
a.add(10)#for adding one value to set
a.update({2,15,7})#for adding more than one value to set
a.discard(10)#for removing value from set
a.remove(6)#for removing value from set
a.pop()#for removing last element from set
print(a)
b=[16,20,45,7,8]
b=set(b)#converting list to set
#Union of two sets
print(a|b)
#intersection of two sets
print(a&b)#1st method
print(a.intersection(b))#second method
c={7,8,15,20}
d={7,9,16}
print(a.intersection_update(b,c,d))#for finding common element in more than 2 sets
#difference between two sets
print(a-c)
#comparision between two sets
print(a<c)
d.clear()#for removing all elements
print(d)





