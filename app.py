from flask import Flask, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Adit@1234",   # 🔴 change this
    database="testdb"
)

# Route to load frontend
@app.route('/')
def home():
    return render_template('index.html')

# API to store name
@app.route('/add', methods=['POST'])
def add_name():
    data = request.get_json()
    name = data.get('name')

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()

    return jsonify({"message": f"{name} stored successfully!"})

if __name__ == '__main__':
    app.run(debug=True)