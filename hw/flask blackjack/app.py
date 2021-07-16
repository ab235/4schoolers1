from flask import Flask, render_template, request, redirect, url_for, session
import csv
from user import User
from blackjack import Card, Deck, Player, Game
import pickle
app = Flask(__name__)
app.secret_key = 'dfghjiouhgyfvhbjaknsdasidnasiodn'

@app.route('/', methods = ['GET', 'POST'])
def index():
    if (request.form.get("Register")):
        return redirect(url_for('register'))
    elif (request.form.get("Login")):
        return redirect(url_for('login'))
    return render_template('index.jinja')
@app.route('/register', methods = ['GET', 'POST'])
def register():
    message = ""
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
                user.save_db('users.csv')
                message = "User registered successfully."
                return redirect(url_for('dashboard', username = username))
            else:
                message = "Password and Confirm Password do not match. User not registered."


    return render_template('register.jinja', message = message)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    message = ""
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.get_user(username, 'users.csv')
        if (user):
            request.user = user
            if (password == user.password):
                session['user'] = username
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
    if (request.method == 'POST'):
        if (request.form.get("deposit")):
            try:
                nmoney = float(request.form.get("amount"))
                if (nmoney > 0):
                    user.money += nmoney
                    user.update('users.csv')
                else:
                    message = "Please deposit a positive amount."
            except TypeError:
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
            except TypeError:
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
    return render_template('dashboard.jinja', user = str(user), message = message)

@app.route('/blackjack/<username>', methods = ['GET', 'POST'])
def blackjack(username):
    message = ""
    user = User.get_user(username, 'users.csv')
    user.money = float(user.money)
    next_card = True
    player = Player(username)
    if (user.money > 300):
        user.update('users.csv')
        game = Game(player)
        message += game.turn() + "<br>"
        message += 'Do you want to take a card: <br>'
        if (request.form.get("exit")):
            return redirect(url_for('end_game', username = username, player = pickle.dumps(player), game = pickle.dumps(game), message = message))
        if (request.form.get("next")):
            return redirect(url_for('catch1', username = username, player = pickle.dumps(player), game = pickle.dumps(game), message = message))
    return render_template('blackjack.jinja', user = str(user), message = message)
@app.route('/catch1/<username>/<player>/<game>/<message>', methods = ['GET', 'POST'])
def catch1(username, player, game, message):
    game = pickle.loads(game)
    player = pickle.loads(player)
    message += game.turn() + "<br>"
    message += 'Do you want to take a card: <br>'
    if (request.form.get("exit")):
        return redirect(url_for('end_game', username = username, player = pickle.dumps(player), game = pickle.dumps(game), message = message))
    elif (request.form.get("next")):
        return redirect(url_for('catch1', username = username, player = pickle.dumps(player), game = pickle.dumps(game), message = message))
    return render_template('blackjack.jinja', user = str(user), message = message)
@app.route('/end_game/<username>/<player>/<game>/<message>', methods = ['GET', 'POST'])
def end_game(username, player, game, message):
    game = pickle.loads(game)
    player = pickle.loads(player)
    payoff = game.stop()
    message += 'You won: $' + str(payoff) + '<br>'
    user = User.get_user(username, 'users.csv')
    user.money += payoff - 100
    user.update('users.csv')
    message += ('do you want to play another game: <br>')
    if (request.form.get("exit")):
        return redirect(url_for('dashboard/<username>', username = username))
    elif (request.form.get("next")):
        return redirect(url_for('blackjack/<username>', username = username))
    return render_template('blackjack.jinja', user = str(user), message = message)
if __name__ == '__main__':
   app.run()
