from flask import Flask, request, jsonify, Response
import sqlite3

app = Flask(__name__)


@app.route('/api/account_info', methods=['GET'])
def get_account_info():

    full_name = request.args.get('full_name')
    sql = f"SELECT * FROM clients WHERE full_name = ?"

    conn = sqlite3.connect('BankClients.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (full_name,))
        result = cursor.fetchall()

        if len(result) == 1:
            row = result[0]
            account_info = {
                "account_number": row[7],
                "account_holder_name": row[1],
                "current_balance": row[8],
                "age": row[2],
                "gender": row[3],
                "reg_contact_no": row[5],
                "email_address": row[6],
                "residence_city": row[4]
            }
            return jsonify(account_info)
        else:
            return jsonify({"error": "Account not found."})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
if __name__ == "__main__":
    app.run(debug=True, port=8080)
