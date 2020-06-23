#for opening file
import os
f=open("file.txt","r")
if f:
    print("file opened successfully")
#r=f.read()
#r1=f.readline()
#print(r)#printing data inside file on console
#print(r1)
#looping through the file
for i in f:
    print(i)
#Writing inside file
f1=open("file.txt","a")
"""
f1.write(" ")
f1.write("5678")"""
print(f1.tell())  # current position of file pointer f1
f1.seek(4) #for changing postion of file pointer f
print(f1.tell())
f1.close()
#for creating new file
"""f2=open("file1.txt","x")
f2.write("123456")
f2.write("78910")
f2.close()"""
#for renaming the file
"""
os.rename("file4.txt","file2.txt")#name of file changes from file4 to file2"""
#for removing the file
os.remove("file2.txt")
#for closing the file
f.close()