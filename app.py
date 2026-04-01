from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="demo_user",
        password="password",
        database="demo_db"
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form.get('name')
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        message = f"Hello, {name} 👋"

    cursor.execute("SELECT name FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', message=message, users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)