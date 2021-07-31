from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'dfghjiouhgdashswevnohshshshidnasiodn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payrollthree.db'
db = SQLAlchemy(app)

class Company(db.Model):
    db.__tablename__ = 'company'
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    admin_id = db.Column(db.String(200))
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
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    ssn = db.Column(db.Integer, nullable=False)
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
        return str(self.uname)

    def is_admin(self):
        id_list = self.company.admin_id
        id_list = id_list.split(",")
        id_list = [int(x) for x in id_list]
        if (self.id in id_list):
            return True
        return False

    @staticmethod
    def save_db(user, db):
        db.session.add(user)
        db.session.commit()
    @staticmethod
    def update(user, ssn, db):
        emps = Company.query.filter_by(name=user.company.name).first().employees
        for i in range(len(emps)):
            if (lis[i].ssn == ssn):
                return lis[i]
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
    @staticmethod
    def get_user_l(uname, lis):
        for i in range(len(lis)):
            if (lis[i].uname == uname):
                return lis[i]
        return False
    def pay_user(self, id):
        user = User.query.filter_by(id=id).first()
        if (user.company.balance - user.salary < 0):
            return False
        user.balance += user.salary
        user.company.balance -= user.salary
        db.session.commit()
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
            company.name = name
            company.balance = money
            Company.save_db(company, db)
            first = User()
            first.name = "()"
            first.ssn = -1
            first.uname = "root"
            first.password = "1234"
            first.salary = 0.0
            first.rating = 0.0
            first.attendance = 0.0
            first.level = 1
            first.balance = 0.0
            first.company = company
            company.employees.append(first)
            company.admin_id = str(first.id)
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
        company = Company.get_company(company_name, db)
        if (company):
            if (User.get_user_l(username, company.employees)):
                if (User.get_user_l(username, company.employees).password == password):
                    session['user'] = username
                    if (User.get_user_l(session['user'], company.employees).is_admin()):
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
    if (Company.get_company(name, db)):
        emps = Company.get_company(name, db).employees
        message = Company.get_company(name, db).balance
        if (session['user']):
            if (User.get_user_l(session['user'], emps)):
                if (User.get_user_l(session['user'], emps).is_admin()):
                    return render_template('dashboard.jinja', message = message, emps = emps)
    return redirect(url_for('index'))
@app.route('/pay/<cname>/<name>', methods = ['GET', 'POST'])
def pay(cname, name):
    if (session['user']):
        if (Company.get_company(cname, db)):
            company = Company.get_company(cname, db)
            emps = company.employees
            if (User.get_user_l(session['user'], emps)):
                if (User.get_user_l(session['user'], emps).is_admin()):
                    company = Company.get_company(cname, db)
                    emps = company.employees
                    admin = User.get_user_l(session['user'], emps)
                    id = User.get_user(name, db).id
                    admin.pay_user(id)
                    return redirect(url_for('dashboard', name = cname))
    return redirect(url_for('index'))
@app.route('/profile/<cname>/<name>', methods = ['GET', 'POST'])
def profile(cname, name):
    if (Company.get_company(cname, db)):
        emps = Company.get_company(cname, db).employees
        if (session['user']):
            if (User.get_user_l(session['user'], emps)):
                user = User.get_user_l(session['user'], emps)
                return render_template('profile.jinja', user=User.get_user_l(name, emps))
    return render_template('index.jinja')
@app.route('/ruser/<name>', methods = ['GET', 'POST'])
def ruser(name):
    if (Company.get_company(name, db)):
        emps = Company.get_company(name, db).employees
        message = ''
        check = False
        if (session['user']):
            if (User.get_user_l(session['user'], emps)):
                if (User.get_user_l(session['user'], emps).is_admin()):
                    if (request.method == "POST"):
                        admini = request.form.get('admin')
                        name = request.form.get('name')
                        ssn = request.form.get('ssn')
                        uname = request.form.get('uname')
                        if (True):
                            password = request.form.get('password')
                            salary = request.form.get('salary')
                            attendance = request.form.get('attendance')
                            rating = request.form.get('rating')
                            level = request.form.get('level')
                            company = User.get_user_l(session['user'], emps).company
                            list1 = [name, ssn, password, salary, attendance, rating, level]
                            for i in range(len(emps)):
                                if (emps[i].uname == uname):
                                    list2 = [emps[i].name, emps[i].ssn, emps[i].password, emps[i].salary, emps[i].attendance, emps[i].rating, emps[i].level]
                                    for j in range(len(list1)):
                                        if (list1[j] != ""):
                                            list2[j] = list1[j]
                                    if (len(admini) > 0 and not emps[i].is_admin()):
                                        emps[0].company.admin_id += "," + str(emps[i].id)
                                    if (len(admini) == 0 and emps[i].is_admin()):
                                        ad_list = emps[0].company.admin_id.split()
                                        ad_list.remove(str(emps[i].id))
                                        emps[0].company.admin_id = ",".join(ad_list)
                                    check = True
                                    db.session.commit()
                                    break
                            if (not check):
                                check = True
                                for j in range(len(list1)):
                                    if (list1[j] == ""):
                                        check = False
                                if (check):
                                    user = User()
                                    user.name = name
                                    user.ssn = ssn
                                    user.uname = uname
                                    user.password = password
                                    user.salary = salary
                                    user.attendance = attendance
                                    user.rating = rating
                                    user.level = level
                                    user.balance = 0.0
                                    user.company = User.get_user_l(session['user'], emps).company
                                    User.save_db(user, db)
                                else:
                                    message = "Spots empty."
                            return redirect(url_for('dashboard', name = emps[0].company.name))
                        else:
                            message = "Username taken."


                    return render_template("ruser.jinja", message = message)




if __name__ == '__main__':
    #db.create_all()
    app.run(use_reloader=False)
