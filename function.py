def sum(a,b):
    print(a+b)

sum(5,8)

t=(5,7,8,10)
#updating tuples
def tuple_list_add(t):
    t=list(t)
    t.append(11)
    t.append(12)
    t=tuple(t)
    print(t)

tuple_list_add(t)

def reverse_string(s):
    print(s[::-1])

reverse_string('Aniruddha')
#Complex number
k=complex(4,7)
print(k)
#divmod function
a,b = divmod(10,2) 
print(a)#prints remainder and  quotient
#Enumerate function
z=[3,5,7,9]
p=enumerate(z)
print(list(p))
#filter function
def filter_func(x):
    if x>20 and x<30:
        return x

li=(24,35,25,45,26,28)
k=filter(filter_func,li)
print(list(k))

#to convert integer to hexadecimal form
a=45
print(hex(a))
#octal form
print(oct(a))
#Python next() function is used to fetch next item from the collection
j=iter([24,333,32])
i=next(j)
print(i)
i=next(j)
print(i)
#Mapping two list using zip function
t=[4,5,6]
s=['four','five','six']
res=zip(t,s)
print(set(res))









