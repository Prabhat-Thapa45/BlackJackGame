import random

import requests
from flask import Flask, Request, Response, render_template, redirect, url_for, flash, request
from constants import get_balance, update_balance, get_bet_amount
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdfsfer34353"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('board'))
    return render_template("form.html")


def get_cards():
    return randint(1, 11, 5)


@app.route('/playing', methods=["GET", "POST"])
def board():
    balance = get_balance()
    bet_amount = get_bet_amount()
    if request.method == "POST":
        if request.form['another_card']:
            return render_template("board.html", balance=balance, bet_amount=bet_amount, cards=cards)
    if bet_amount > 20:
        cards = get_cards()
        return render_template("board.html", balance=balance, bet_amount=bet_amount, cards=list(cards))
    return render_template("board.html", balance=balance, bet_amount=bet_amount)


@app.route('/bet', methods=["POST"])
def manage_money():
    if request.method == "POST":
        balance = get_balance()
        bet_amount = int(request.form["bet_amount"])
        if bet_amount > balance or bet_amount < 20:
            return redirect(url_for("board"))
        update_balance(bet_amount)
        return redirect(url_for("board"))


@app.route('/play')
def play():
    return render_template('board.html', balance=get_balance())


if __name__ == "__main__":
    app.run(debug=True)
