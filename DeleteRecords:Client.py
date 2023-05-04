import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="BankClients"
)
mycursor = mydb.cursor()

sql = "DELETE FROM clients WHERE full_name = 'Angel'"

#mycursor.execute(sql)
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record deleted")