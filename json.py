import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20,  
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]  
}  
b = json.dumps(student)  
print(b)
#converting python objects to json object
with open("data.json","w") as write_file:  
    json.dump(student,write_file)  

with open("data.json", "r") as read_file:  
    c = json.load(read_file)#converting json object to python object  
    
print(c)