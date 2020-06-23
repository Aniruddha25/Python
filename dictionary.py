student = {"Name":"Aniruddha","age":22}
print(student["Name"])
#For printing key-value pair
for i,j in student.items():
    print(i,j)

#student.clear() -- removing all key-value pairs
print(len(student))#length of dictionary
#For adding key-value pair to existing dictionary
student.update({"Degree":"Mechanical"})
print(student)
student.popitem()#for removing last key-value pair
print(student)
#student.keys() for printing keys
#student.values() for printing values