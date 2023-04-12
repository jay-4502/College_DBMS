import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jay4502",
    database="college"
)

mycursor=mydb.cursor()
sql="Insert into student(ccode,id,fname,lname,sem,email,phno,gender,branch,aadharno)values(%s,%d,%s,%s,%d,%s,%s,,%s)"
val=('BG186',020,'jayasri','a',5,'ajanu9926@gmail.com','9845211803','female','aiml','592714723243')
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")