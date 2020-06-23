import itertools
#count
for i in itertools.count(10,4):  
    if i == 50:  
        break  
    else:  
        print(i,end=" ") 
#Zip function
a=[i for i in range(6)]
b=[1,2,3,4,5,6]
z=zip(a,b)
print(z)
#cycle
temp = 0  
for i in itertools.cycle("1234"):  
    if temp > 5:  
        break  
    else:  
        print(i,end=' ')  
        temp = temp+1  
#Repeating values
print("Printing the number repeadtly:")  
print(list(itertools.repeat(40,10)))  
#product()
from itertools import product,permutations,combinations
print(list(product([1, 2,3], repeat=2))) #cartesian product with self
print(list(product([1,2,3,4],[2,3])))
print(list(product('cde',[1,2,3])))
print(list(permutations([1,2,3],2)))
print(list(permutations('ABC')))
print(list(permutations(range(3),2)))
print(list(combinations('ABCD',3)))
l1=[4,5,6,7,8]
#Accumulate
import operator
print(list(itertools.accumulate(l1)))
print(list(itertools.accumulate(l1,operator.mul)))
l2=[720,6,5,4,3,2,1]
print(list(itertools.accumulate(l2,operator.floordiv)))
print(list(itertools.chain(l1,l2)))#to concat 2 or more lists
print(list(itertools.dropwhile(lambda x: x%2==0,l1)))#It drops  true conditon untill false statement begins 
print(list(itertools.filterfalse(lambda x: x%2==0,l1)))#It drops all false statements
print(list(itertools.takewhile(lambda x: x%2==0,l2)))#It prints true condition untill false condition arrives ie.reverse of dropwhile

#starmap function
l3=[(23,5,19),(20,24),(25,28)]
print(list(itertools.starmap(max,l3)))
print(list(itertools.starmap(min,l3)))













