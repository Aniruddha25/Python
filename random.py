
import random as r
print(r.random())# number between 0 to 1
print(r.randint(30,40))#number between specified range
k=r.randrange(5,15,2)#between start and end considering stepsize
print(k)
#random.choice - selects element from given list randomly
l=[10,30,34,23,18]
print(r.choice(l))
#Before shuffling
print(l)
r.shuffle(l)#change the sequence of elements in the list/tuple
#After shuffling
print(l)
