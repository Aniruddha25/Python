import re
str ="My Name is Aniruddha"
#This method returns a list containing a list of all matches of a pattern within the string.
 # It returns the patterns in the order they are found.If there are no matches, then an empty list is returned.
m=re.findall("Name",str)
print(m)
#The match object contains the information about the search and the output. If there is no match found, the None object is returned.
n=re.search("My",str)
print(n)
print(n.span())
print(n.group())


