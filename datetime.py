import time
#Time functionalities
print(time.time())
time.sleep(2)#temperary stopping execution of program
print(time.localtime(time.time()))#current time
#formatted time
print(time.asctime(time.localtime(time.time())))

