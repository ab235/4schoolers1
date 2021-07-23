from flask import Flask, render_template, request, redirect, url_for, session
import csv
from user import User
from blackjack import Card, Deck, Player, Game
app = Flask(__name__)
app.secret_key = 'dfghjiouhgdashswevnohshshshidnasiodn'
player = Player('none')
game = Game(player)
@app.route('/', methods = ['GET', 'POST'])
def index():
    #if (request.form.get("Register")):
        #return redirect(url_for('register'))
    #elif (request.form.get("Login")):
        #return redirect(url_for('login'))
    session['user'] = False
    return render_template('index.jinja')
@app.route('/register', methods = ['GET', 'POST'])
def register():
    message = "Register"
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        cpassword = request.form.get('confirm password')
        usernames = []
        for row in User.read_file('users.csv'):
            usernames.append(row[0])
        if (username in usernames):
            message = "This username is already taken. Please try again."
        else:
            if (password == cpassword):
                user = User(username, password)
                session['user'] = user.username
                user.save_db('users.csv')
                message = "User registered successfully."
                return redirect(url_for('dashboard', username = username))
            else:
                message = "Password and Confirm Password do not match. User not registered."


    return render_template('register.jinja', message = message)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    message = "Login"
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.get_user(username, 'users.csv')
        if (user):
            request.user = user
            session['user'] = user.username
            if (password == user.password):
                return redirect(url_for('dashboard', username = username))
            else:
                message = 'Password does not match.'
        else:
            message = "User does not exist."

        

    return render_template('login.jinja', message = message)
@app.route('/dashboard/<username>', methods = ['GET', 'POST'])
def dashboard(username):
    user = User.get_user(username, 'users.csv')
    message = ''
    user.money = float(user.money)
    if (session['user']):
        if (request.method == 'POST'):
            if (request.form.get("deposit")):
                try:
                    nmoney = float(request.form.get("amount"))
                    if (nmoney > 0):
                        user.money += nmoney
                        user.update('users.csv')
                    else:
                        message = "Please deposit a positive amount."
                except ValueError:
                    message = "This is not a depositable number."
            if (request.form.get("withdraw")):
                try:
                    nmoney = float(request.form.get("amount"))
                    if (nmoney > 0 and (user.money - nmoney) >= 0):
                        user.money -= nmoney
                        user.update('users.csv')
                    elif (nmoney < 0):
                        message = "Please withdraw a positive amount of money."
                    else:
                        message = "You can't afford this withdrawal."
                except ValueError:
                    message = "This is not a withdrawable number."
            if (request.form.get("change_password")):
                npass = request.form.get("new_password")
                cpass = request.form.get("confirm_password")
                if (npass == cpass):
                    user.password = npass
                    user.update('users.csv')
                else:
                    message = "Passwords do not match."
            if (request.form.get("play")):
                return redirect(url_for('blackjack', username = username))
            if (request.form.get("logout")):
                session['user'] = False
                return redirect(url_for('index'))
        return render_template('dashboard.jinja', user = str(user), message = message)
    else:
        return redirect(url_for('index'))

@app.route('/blackjack/<username>', methods = ['GET', 'POST'])
def blackjack(username):
    if (session['user']):
        session['message'] = ""
        user = User.get_user(username, 'users.csv')
        user.money = float(user.money)
        next_card = True
        player.name = username
        if (user.money >= 300):
            session['message'] += 'Do you want to take a card: <br>'
            if (request.form.get("exit")):
                return redirect(url_for('end_game', username = username))
            if (request.form.get("next")):
                session['message'] += game.turn() + "<br>"
                return redirect(url_for('catch1', username = username))
        else:
            session['message'] = "You don't have enough funds."
            if (request.form.get("exit")):
                return redirect(url_for('dashboard', username = username))
        return render_template('blackjack.jinja', user = str(user), message = session['message'])
    else:
        return redirect(url_for('index'))
@app.route('/catch1/<username>', methods = ['GET', 'POST'])
def catch1(username):
    if (session['user']):
        if (not game.game_over()):
            user = User.get_user(username, 'users.csv')
            session['message'] += 'Do you want to take a card: <br>'
            if (request.form.get("exit")):
                return redirect(url_for('end_game', username = username))
            elif (request.form.get("next")):
                session['message'] += game.turn() + "<br>"
                return redirect(url_for('catch1', username = username))
        else:
            return redirect(url_for('end_game', username = username))
        return render_template('blackjack.jinja', user = str(user), message = session['message'])
    else:
        return redirect(url_for('index'))
@app.route('/end_game/<username>', methods = ['GET', 'POST'])
def end_game(username):
    if (session['user']):
        payoff = game.stop()
        if (payoff-100 < 0):
            session['message'] += 'You lost: $' + str(100 - payoff) + '<br>'
        else:
            session['message'] += 'You won: $' + str(payoff-100) + '<br>'
        user = User.get_user(username, 'users.csv')
        user.money = float(user.money)
        user.money += payoff - 50
        user.update('users.csv')
        player.cards = []
        game.__init__(player)
        session['message'] += ('do you want to play another game: <br>')
        if (request.form.get("exit")):
            return redirect(url_for('dashboard', username = username))
        elif (request.form.get("next")):
            return redirect(url_for('blackjack', username = username))
        return render_template('blackjack.jinja', user = str(user), message = session['message'])
    else:
        return redirect(url_for('index'))
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    if (request.method == 'POST'):
        return redirect(url_for('index'))
    return render_template('404.jinja'), 404
if __name__ == '__main__':
   app.run()
