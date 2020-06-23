s= lambda p,q:p+q
print(s(10,20))

r=lambda p,q: divmod(p,q)
print(r(20,10))
#for performing operation on entire list
l=[20,10,15,3]
t=lambda    x: x*3
print(list(map(t,l)))