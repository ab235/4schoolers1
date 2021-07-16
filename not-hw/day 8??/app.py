from flask import Flask, render_template, request
import csv
import user
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.jinja")

@app.route('/users')
def users():
    data = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    return render_template("users.jinja", data = data)

@app.route('/register', methods = ['GET', "POST"])
def register():
    if (request.method == "POST"):
        fname = request.form.get(fname)
        lname = request.form.get(lname)
        email = request.form.get(em)
        username = request.form.get(uname)
        pw = request.form.get(pw)
        apee = User(fname, lname, email, username, pw)
        apee.save_db()
    return render_template('register.jinja')

@app.route('/login')
def login():
    return render_template('login.jinja')

if (__name__ == "__main__"):
    app.run()
