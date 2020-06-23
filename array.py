from array import array
a=array('i',[10,34,35,23,45])
#Changing array elements
a[0]=11
a[3]=20
#Deleting array element
del a[4]
#list operations that can be performed on both array and list
a.pop(2)#for removing element from particular position
a.append(10)#for adding element at last position
print(a)
#length of array
print(len(a))
#array concatenation
b=array('i',[4,6,7,8])
c=array('i')
c=a+b
print(c)


