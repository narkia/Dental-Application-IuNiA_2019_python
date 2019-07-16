import MySQLdb

mydb = MySQLdb.connect(  host="localhost",   user="yourusername",   passwd="yourpassword" )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")