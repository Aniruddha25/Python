def add(x,y):
    return x+y

def div(x,y):
    return x/y
##Function as argument
def operation(func,x,y):
    return func(x,y)

print(operation(add,10,5))
print(operation(div,10,5))
#Function inside another function
def msg():
    def hello():
        print("Hello")
    hello()


msg()