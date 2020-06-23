class cricketer:
    name ="Virat"
    age=32

    def __init__(self,name,age):#Parameterized constructor
        self.name = name
        self.age =age

    def display(self):
          print("Name :",self.name)
          print("Age :",self.age)
    
    


c= cricketer("Rohit",33)#Creation of object
c.display()



      
