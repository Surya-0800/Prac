import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Surya@180",database="MYDB")

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE MYDB")

# mycursor.execute("CREATE TABLE MYDATA(name VARCHAR(255),adress VARCHAR(255))")

sql = "INSERT INTO MYDATA (name,adress)VALUES(%s,%s)"
val = ("Surya","Kadapa")

mycursor.execute(sql,val)
mydb.commit()