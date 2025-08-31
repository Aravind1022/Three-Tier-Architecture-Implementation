from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="<db-vm-private-ip>",
        user="demo_user",
        password="demo_pass",
        database="demo_db"
    )

@app.route('/message')
def message():
    return jsonify({"message": "Backend is working!"})

@app.route('/users')
def users():
    try:
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, name FROM users")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
