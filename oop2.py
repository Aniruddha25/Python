class student:
    name = "Aniruddha"
    age=22
    gender ="Male"
    def __init__(self):
        self.name="Anil"
        self.age=23
        self.gender="Male"
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender :",self.gender)


s= student()
s.display()
#Getter-setters in python
print(getattr(s,'age'))#to get attribute value 
setattr(s,'age',22)#to change the value of attribute / variable
print(getattr(s,'age'))
#delattr(s,'gender') -- for deleting attribute
print(hasattr(s,'name'))# object has attribute or not returns true or false
# Buit in class attributes
print(s.__dict__)#print attributes and its value in dictionary form
print(s.__module__)
print(s.__doc__)



