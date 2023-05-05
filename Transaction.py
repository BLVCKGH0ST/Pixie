import mysql.connector
from decimal import Decimal

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="BankClients"
)

# Creating a cursor object to interact with the database
mycursor = mydb.cursor()

# Getting the sender's information
sender_name = input("Enter sender's name: ")
sender_query = "SELECT * FROM clients WHERE full_name=%s"
mycursor.execute(sender_query, (sender_name,))
sender_info = mycursor.fetchone()
if not sender_info:
    print("Sender's information not found!")
    exit()

# Getting the receiver's information
receiver_name = input("Enter receiver's name: ")
receiver_acc_no = input("Enter receiver's account number: ")
receiver_query = "SELECT * FROM clients WHERE full_name=%s AND account_number=%s"
mycursor.execute(receiver_query, (receiver_name, receiver_acc_no))
receiver_info = mycursor.fetchone()
if not receiver_info:
    print("Receiver's information not found!")
    exit()

transfer_amount = float(input("Enter transfer amount: "))

# Checking if the sender has enough balance
if float(sender_info[7]) < transfer_amount:
    print("Insufficient balance in sender's account!")
    exit()

# Updating the sender's balance
#sender_balance = sender_info[7] - transfer_amount
sender_balance = sender_info[7] - Decimal(str(transfer_amount))
sender_update_query = "UPDATE clients SET balance=%s WHERE full_name=%s"
mycursor.execute(sender_update_query, (sender_balance, sender_info[0]))
mydb.commit()

# Updating the receiver's balance
# #receiver_balance = receiver_info[7] + transfer_amount
receiver_balance = receiver_info[7] + Decimal(str(transfer_amount))
receiver_update_query = "UPDATE clients SET balance=%s WHERE full_name=%s"
mycursor.execute(receiver_update_query, (receiver_balance, receiver_info[0]))
mydb.commit()

print("Transaction successful!")
print("Sender: ", sender_info[0], "(", sender_info[6], ")", " Balance: ", sender_balance)
print("Receiver: ", receiver_info[0], "(", receiver_info[6], ")", " Balance: ", receiver_balance)

mycursor.close()
mydb.close()
