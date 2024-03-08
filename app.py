from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


x = 0


def createapp():
    app = Flask(__name__, template_folder='template')

    return app


app = createapp()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/intro', methods=['GET', 'POST'])
def intro():
    return render_template("intro.html")


@app.route('/question1', methods=['GET', 'POST'])
def q1():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Spend it all, YOLO':
            x += 100
        elif answer == 'Decline the invitation':
            x += 10
        elif answer == 'Save some and decide to make up for the money spent another day':
            x += 60
        else:
            x += 20
        return redirect('/question2')
    return render_template("question1.html")


@app.route('/question2', methods=['GET', 'POST'])
def q2():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Open an account with Bank A':
            x += 20
        elif answer == 'Open an account with Bank B':
            x += 100
        elif answer == 'Open an account with both banks and use them for different purposes':
            x += 10
        else:
            x += 60
        return redirect('/question3')
    return render_template("question2.html")


@app.route('/question3', methods=['GET', 'POST'])
def q3():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Buy from A and consider it as an investment in your long-term health and well-being':
            x += 20
        elif answer == 'Buy from B and save money for other expenses or goals':
            x += 50
        elif answer == 'Buy from both and balance your budget and nutrition':
            x += 40
        else:
            x += 10
        return redirect('/question4')
    return render_template("question3.html")


@app.route('/question4', methods=['GET', 'POST'])
def q4():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Buy raw ingredients and spend more time making a meal':
            x += 20
        elif answer == 'Buy readymade snacks and drinks and enjoy it whenever you want':
            x += 100
        elif answer == 'Look for another store with prices and options':
            x += 10
        else:
            x += 40
        return redirect('/question5')
    return render_template("question4.html")


@app.route('/question5', methods=['GET', 'POST'])
def q5():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Go with them and release the accumulated stress from your studies':
            x += 60
        elif answer == 'Decline them saying you have some other arrangements and save the money for rainy day':
            x += 40
        elif answer == 'Ask for help from your friends and family to sponsor you for this trip':
            x += 10
        else:
            x += 100
        return redirect('/question6')
    return render_template("question5.html")


@app.route('/question6', methods=['GET', 'POST'])
def q6():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Use public transport as you are worried about your bike being stolen':
            x += 20
        elif answer == 'Buy the bike to save your time invest in your health and go green':
            x += 40
        elif answer == 'Look for another option with better efficiency and reliability':
            x += 10
        else:
            x += 80
        return redirect('/question7')
    return render_template("question6.html")


@app.route('/question7', methods=['GET', 'POST'])
def q7():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Buy it from the branded shop or Amazon and look good':
            x += 80
        elif answer == 'Buy it from TEMU or 2nd hand events but not sure about the quality and if you would find something that you really like':
            x += 100
        elif answer == 'Buy from both at one time and then decide which platform you would want to use for future':
            x += 20
        else:
            x += 40
        return redirect('/question8')
    return render_template("question7.html")


@app.route('/question8', methods=['GET', 'POST'])
def q8():
    answer = str(request.form.get('choice'))
    if request.method == 'POST':
        global x
        if answer == 'Buy a plain sweater and look more professional in events that you attend':
            x += 10
        elif answer == 'Buy the patterned sweater and brighten up your mood as you have no professional business - Charles':
            x += 10
        elif answer == 'Buy both sweaters and wear them when required':
            x += 80
        else:
            x += 100
        return redirect('/character')
    return render_template("question8.html")


@app.route('/character', methods=['GET', 'POST'])
def character():
    global x

    if x > 0 and x <= 100:
        characterName = 'Holt'
    elif x > 400 and x <= 500:
        characterName = 'Rosa'
    elif x > 100 and x <= 200:
        characterName = 'Amy'
    elif x > 200 and x <= 300:
        characterName = 'Charles'
    elif x > 300 and x <= 400:
        characterName = 'Terry'
    elif x > 500 and x <= 600:
        characterName = 'Gina'
    else:
        characterName = 'Jake'

    x = 0

    if characterName == 'Jake':
        return render_template('Jake_Peralta.html')
    elif characterName == 'Holt':
        return render_template('Holt.html')
    elif characterName == 'Rosa':
        return render_template('Rosa.html')
    elif characterName == 'Amy':
        return render_template('Amy.html')
    elif characterName == 'Charles':
        return render_template('Charles.html')
    elif characterName == 'Terry':
        return render_template('Terry.html')
    elif characterName == 'Gina':
        return render_template('Rosa.html')
    else:
        return render_template('character.html')


@app.route('/moderately_conservative')
def moderately_conservative_risk_taker():
    return render_template('moderately_conservative_risk_taker.html')


@app.route('/moderately_aggresive')
def moderately_aggresive_risk_taker():
    return render_template('moderately_aggresive_risk.html')


@app.route('/moderately_risk')
def moderately_risk_taker():
    return render_template('moderately_risk_taker.html')


@app.route('/aggresive')
def aggresive_risk_taker():
    return render_template('aggresive_risk_taker.html')


@app.route('/conservative')
def conservative_risk_taker():
    return render_template('conservative_risk_taker.html')


if __name__ == "__main__":
    app.run(debug=True)
