a=5
b=10
try:
    c=a/b
    print(float(c))
except dividebyzeroerror:
    print("Divide by zero error")
else:
    print("Exception not found")