from flask import Flask, jsonify, request
import sqlite3
import random

app = Flask(__name__)


# Define the API endpoints
@app.route('/')
def home():
    return 'Welcome to Pixie!'


@app.route('/api/clients_create', methods=['POST'])
def create_client():
    conn = sqlite3.connect('BankClients.db')
    cursor = conn.cursor()

    data = request.get_json()
    full_name = data['full_name']
    age = data['age']
    gender = data['gender']
    residence_city = data['residence_city']
    phone = data['phone']
    email = data['email']
    balance = data['balance']
    pin = data['PIN']
    account_number = random.randint(1000000000, 9999999999)

    # Create a new account
    sql = "INSERT INTO clients (full_name, age, gender, residence_city, phone, email, balance, PIN, account_number) " \
          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    val = (full_name, age, gender, residence_city, phone, email, balance, pin, account_number)

    try:
        cursor.execute(sql, val)
        conn.commit()

        # Return the newly created client
        client_id = cursor.lastrowid
        sql = "SELECT * FROM clients WHERE id = ?"
        cursor.execute(sql, (client_id,))
        result = cursor.fetchone()

        conn.close()
        return jsonify(result)

    except sqlite3.Error as error:
        return jsonify({"error": str(error)})


@app.route('/api/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    conn = sqlite3.connect('BankClients.db')
    cursor = conn.cursor()

    sql = "SELECT * FROM clients WHERE id = ?"
    cursor.execute(sql, (client_id,))
    result = cursor.fetchone()

    conn.close()
    return jsonify(result)


@app.route('/api/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    conn = sqlite3.connect('BankClients.db')
    cursor = conn.cursor()

    data = request.get_json()
    sql = "UPDATE clients SET full_name = ?, age = ?, gender = ?, residence_city = ?, phone = ?, email = ?, " \
          "balance = ?, PIN = ? WHERE id = ?"
    val = (data['full_name'], data['age'], data['gender'], data['residence_city'], data['phone'], data['email'],
           data['balance'], data['PIN'], client_id)
    cursor.execute(sql, val)
    conn.commit()

    conn.close()
    return jsonify({'message': 'Client updated successfully'})


@app.route('/api/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    conn = sqlite3.connect('BankClients.db')
    cursor = conn.cursor()

    sql = "DELETE FROM clients WHERE id = ?"
    cursor.execute(sql, (client_id,))
    conn.commit()

    conn.close()
    return jsonify({'message': 'Client deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=5010)