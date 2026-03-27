from flask import Flask, render_template, request
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "SQL@Acc#aprajita93",
    database = "flask_db"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template("Index.html")

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    # Validation
    if not username or not password :
        return "All fields are required !!"

    # Hash Password
    hashed_password = generate_password_hash(password)

    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query,(username, hashed_password))
        db.commit()
        return "Signup Successfully !!"
    except Exception as e:
        return str(e)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    #Validation
    if not username or not password :
        return "All fields are required !!"

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        stored_password = user[2]  #password column
        if check_password_hash(stored_password, password):
            return "Login Successfully !!"
        else:
            return "Wrong Password !!"
    else:
        return "User Not Found !!"
        
if __name__ == '__main__':
    app.run(debug=True)