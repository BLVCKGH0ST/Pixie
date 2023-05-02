import mysql.connector

#mydb = mysql.connector.connect({
 # "host": "localhost",
 # "port": 3306,
 # "user": "root",
 # "password": "",
 # "schema": "BankClients"
 # "database"
#})

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="BankClients"
)
mycursor = mydb.cursor()

# Prompt user to enter full name
full_name = input("Enter Full name: ")

# Construct the SQL query to retrieve the account information
sql = f"SELECT * FROM clients WHERE full_name = '{full_name}'"

try:
    # Execute the SQL query and get the result set
    #result = mydb.sql(sql).execute()
    mycursor.execute(sql)
    result = mycursor.fetchall()

    # Check if the account was found in the database
    if len(result) == 1:
        row = result[0]
        print("Account number:", row[6])
        print("Account holder name:", row[0])
        print("Current balance:", row[7])
        print("Age:", row[1])
        print("Gender:", row[2])
        print("Reg. Contact No.:", row[4])
        print("Email address:", row[5])
        print("Residence city:", row[3])
    else:
        print("Account not found")
except mysql.connector.errors.ProgrammingError as e:
    print("Error:", e)

mydb.close()
