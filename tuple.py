
"""Where use tuple
Using tuple instead of list is used in the following scenario.

1. Using tuple instead of list gives us a clear idea that tuple data is constant and must not be changed.

2. Tuple can simulate dictionary without keys. Consider the following nested structure which can be used as a dictionary.

[(101, "John", 22), (102, "Mike", 28),  (103, "Dustin", 30)]   
3. Tuple can be used as the key inside dictionary due to its immutable nature."""
#Nesting of tuple inside list
j=("Aniruddha",21)
k=("Rajat",22)
l=("shrikant",26)
a=[j,l,k]
print(a)

