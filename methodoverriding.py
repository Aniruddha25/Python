class car:
    __p=0
    def running(self):
        print("I am running")

class bmw(car):
    def running(self):
        print("I am running at 100 kmph")


class audi(car):
    def running(self):
        print("I am running at 120 kmph")



a= audi()
a.running()
c=car()
print(c.__p)#"__" this sign is used to hide the data member
