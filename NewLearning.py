from flask import Flask, render_template, request
import mysql.connector

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

    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query,(username, password))
        db.commit()
        return "Signup Successfully !!"
    except:
        return "Username already exists !!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username,password))
    user = cursor.fetchone()

    if user:
        return f"Welcome {username} !! :)"
    else:
        return "Invalid username or password !! :("

if __name__ == '__main__':
    app.run(debug=True)