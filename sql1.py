from mysql.connector import connect
m= connect(host="localhost",user="root",passwd="google")
print(m)
print(m.cursor())
