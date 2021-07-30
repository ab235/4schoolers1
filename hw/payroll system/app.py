from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'dfghjiouhgdashswevnohshshshidnasiodn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Company(db.Model):
    db.__tablename__ = 'company'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    employees = db.relationship("User", back_populates="company", enable_typechecks=False)

    def __repr__(self):
        return self.name

    @staticmethod
    def get_company(name, db):
        return Company.query.filter_by(name=name).first()

    @staticmethod
    def save_db(company, db):
        db.session.add(company)
        db.session.commit()


class User(db.Model):
    db.__tablename__ = 'user'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(50))
    ssn = db.Column(db.Integer, unique=True, nullable=False)
    uname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    attendance = db.Column(db.Float)
    rating = db.Column(db.Float, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship("Company", back_populates="employees")

    def __repr__(self):
        return self.name

    def is_admin(self):
        return False

    @staticmethod
    def save_db(user, db):
        db.session.add(user)
        db.session.commit()
    @staticmethod
    def update(user, db):
        puser = User.query.filter_by(id=user.id).first()
        puser.name = user.name
        puser.ssn = user.ssn
        puser.salary = user.salary
        puser.attendance = user.attendance
        puser.rating = user.rating
        puser.level = user.level
        puser.balance = user.balance
        puser.uname = user.uname
        puser.password = user.password
        db.session.commit()

    @staticmethod
    def get_user(uname, db):
        return User.query.filter_by(uname=uname).first()

class Admin(User):
    def pay_user(id):
        user = User.query.filter_by(id=id).first()
        if (user.company.balance - user.salary < 0):
            return False
        user.balance += user.salary
        user.company.balance -= user.salary
        db.session.commit()
        return True
    @staticmethod
    def register_user(self, name, ssn, uname, password, salary, attendance, rating, level, balance):
        user = User()
        user.id = (len(User.query.filter_by(company = self.company)))
        user.name = name
        user.ssn = ssn
        user.uname = uname
        user.password = password
        user.salary = salary
        user.attendance = attendance
        user.rating = rating
        user.level = level
        user.balance = balance
        user.company = self.company
        User.save_db(user, db)
    def is_admin(self):
        return True

@app.route('/', methods = ['GET', 'POST'])
def index():
    session['user'] = False
    return render_template('index.jinja')
@app.route('/register', methods = ['GET', 'POST'])
def register():
    message = "Register"
    if (request.method == 'POST'):
        name = request.form.get('name')
        money = request.form.get('balance')
        if (Company.get_company(name, db)):
            message = "This name is already taken. Please try again."
        else:
            company = Company()
            company.id = len(Company.query.all())
            company.name = name
            company.balance = money
            company.employees.append(Admin())
            company.employees[0].id = 0
            company.employees[0].name = "_"
            company.employees[0].ssn = -1
            company.employees[0].uname = "root"
            company.employees[0].password = "1234"
            company.employees[0].salary = 0.0
            company.employees[0].rating = 0.0
            company.employees[0].attendance = 0.0
            company.employees[0].level = 1
            company.employees[0].balance = 0.0
            company.employees[0].company = company

            session['user'] = "root"
            Company.save_db(company, db)
            message = "User registered successfully."
            return redirect(url_for('dashboard', name = name))
    return render_template('register.jinja', message = message)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    message = "Login"
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        company_name = request.form.get('company')
        company = db.get_company(company_name, db)
        if (company):
            if (company.employees.get_user(username)):
                if (company.employees.get_user(username).password == password):
                    session['user'] = username
                    if (company.employees.get_user(username).is_admin()):
                        return redirect(url_for('dashboard', name = company.name))
                    else:
                        return redirect(url_for('profile', name = username, cname = company.name))
                else:
                    message = "Password does not match."
            else:
                message = 'User does not exist.'
        else:
            message = "Company does not exist."
    return render_template('login.jinja', message = message)

@app.route('/dashboard/<name>', methods = ['GET', 'POST'])
def dashboard(name):
    if (Company.get_company(name)):
        emps = Company.get_company(name).employees
        message = ''
        if (session['user']):
            if (emps.get_user(session['user'])):
                if (emps.get_user(session['user']).is_admin()):
                    if (request.method == 'POST'):
                        if (request.form.get('new_user')):
                            return redirect(url_for('ruser', name=name))
                        admin = emps.get_user(session['user'])
                        ids = [x.id for x in emps]
                        for x in ids:
                            if (str(x) in request.form):
                                admin.pay_user(x)
                                message = str(emps.filter_by(id=x).first().name) + " has been paid."
                    return render_template('dashboard.jinja', message = message, emps = emps)
    return redirect(url_for('index'))
@app.route('/profile/<cname>/<name>', methods = ['GET', 'POST'])
def profile(cname, name):
    if (Company.get_company(cname)):
        emps = Company.get_company(cname).employees
        if (session['user']):
            if (emps.get_user(session['user'])):
                user = emps.get_user(session['user'])
                return render_template('profile.jinja', user=user)
    return render_template('profile.jinja')
@app.route('/ruser/<name>', methods = ['GET', 'POST'])
def ruser(name):
    if (Company.get_company(name)):
        emps = Company.get_company(name).employees
        message = ''
        if (session['user']):
            if (emps.get_user(session['user'])):
                if (emps.get_user(session['user']).is_admin()):
                    return render_template("profile.jinja")




if __name__ == '__main__':
    app.run(use_reloader=False)
