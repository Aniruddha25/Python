##stack
l=[3,5,6,78,9,10]
#push operation
l.append(13)
l.append(12)
#pop operation
l.pop()
print(l)
##Queue
from queue import Queue
p=Queue(maxsize=10)
p.put(24)
p.put(14)
p.put(54)
p.put(34)
print(p.get())
print(p.get())
print(p.get())
print(p.get())


