class surname:
    sname="Kulkarni"
    def surname_func(self):
        return self.sname



class father(surname):
    name="Mukund"
    def middle_name(self):
        return self.name

f= father()
s=surname()

class myname(father):
    myname="Aniruddha"
   
    def full_name(self):
        fname=" My name is "+self.myname + " "+f.middle_name()+ " "+ s.surname_func()
        print(fname)


i = myname()
print(i.middle_name())
i.full_name()
#Multiple inheritance
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20)) 







    

