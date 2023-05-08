import mysql.connector
import random

# Establish a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="BankClients"
)
mycursor = mydb.cursor()

full_name = input("Enter Full name: ")

sql = f"SELECT * FROM clients WHERE full_name = '{full_name}'"
mycursor.execute(sql)
result = mycursor.fetchall()

if len(result) > 0:
    print("Account already exists")
else:
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    residence_city = input("Enter residence city: ")
    phone = input("Enter registered contact number: ")
    email = input("Enter email address: ")
    balance = float(input("Enter initial balance: "))

    # Generate a random 10-digit account number
    account_number = random.randint(1000000000, 9999999999)

    # Create a new account
    sql = "INSERT INTO clients (full_name, age, gender, residence_city, phone, email, account_number, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (full_name, age, gender, residence_city, phone, email, account_number, balance)
    mycursor.execute(sql, val)
    mydb.commit()

    print("Account created successfully")

# Close database connection
mydb.close()
