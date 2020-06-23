a=b=c=32
print(a,b,c)
a,b,c=32,33,34
print(a,b,c)
# tuples to store  different kind of datatypes
d=(3,7,'a',"Aniruddha")
print(d)
#splitting the tuple
print(d[2:])
#dictionary key-value pair
e={'Name':"aniruddha",'age':22}
print(e)
print(e.keys())
print(e.values())
print(e['Name'])#kind of mapping
#type of variable
print(type(d))
#list
p = [5,6,7,8,9]
print(p[2:4])
p.append(4)
p.sort()
print(p)
#Multiline string
f='Aniruddha \
Mukund \
Kulkarni '
print(f)
#operators
print(6**3)
print(7//3    )#It gives the floor value of the quotient produced by dividing the two operands.
a =  1 and 5 # and,or,not logical operators
a = 2 or 4#takes first no. as op
a= 5 or 3
a= 5 and 1 # Takes second no. as a op
print(a)
#Membership operator in and not in 
if 3 in p:
    p.remove(4)
    print(p)
elif 2 not in p:
    print(2)

    
if 4 in p:
    print(p)
else:
    print(p+p)


