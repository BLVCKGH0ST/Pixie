from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route('/api/transfer', methods=['POST'])
def transfer():
    conn = sqlite3.connect("BankClients.db")
    cursor = conn.cursor()

    data = request.get_json()
    sender_name = data['sender_name']
    receiver_name = data['receiver_name']
    receiver_acc_no = data['receiver_acc_no']
    transfer_amount = data['transfer_amount']

    sender_query = "SELECT * FROM clients WHERE full_name=?"
    cursor.execute(sender_query, (sender_name,))
    sender_info = cursor.fetchone()
    if not sender_info:
        return jsonify({'message': 'Incorrect Information entered'}), 404

    receiver_query = "SELECT * FROM clients WHERE full_name=? AND account_number=?"
    cursor.execute(receiver_query, (receiver_name, receiver_acc_no))
    receiver_info = cursor.fetchone()
    if not receiver_info:
        return jsonify({'message': 'Account not found'}), 404

    if sender_info[7] < transfer_amount:
        return jsonify({'message': 'insufficient balance in your account'}), 400

    # sender_balance = str(sender_info[7] - transfer_amount)
    sender_balance = str(sender_info[7] - transfer_amount)
    sender_update_query = "UPDATE clients SET balance=? WHERE full_name=?"
    cursor.execute(sender_update_query, (sender_balance, sender_info[0]))
    conn.commit()

    receiver_balance = str(receiver_info[7] + transfer_amount)
    receiver_update_query = "UPDATE clients SET balance=? WHERE full_name=?"
    cursor.execute(receiver_update_query, (receiver_balance, receiver_info[0]))
    conn.commit()

    return jsonify({
        'sender': sender_info[1],
        'sender_balance': str(sender_info[8] - transfer_amount),
        'receiver': receiver_info[1],
        'transfer_amount': transfer_amount,
        'message': 'Transfer completed successfully.'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=7007)
