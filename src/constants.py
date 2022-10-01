import json
from numpy.random import randint


def generate_cards():
    return randint(1,10,5)

CARDS = generate_cards()

def get_cards():
    


print(get_cards())

def get_balance() -> int:
    with open("constants.json") as file:
        data = json.load(file)
        return int(data["AMOUNT"])


def get_bet_amount() -> int:
    with open("constants.json") as file:
        data = json.load(file)
        return int(data["BET_AMOUNT"])


def update_balance(bet_amount):
    with open("constants.json", "r+") as file:
        data = json.load(file)
        data["AMOUNT"] -= bet_amount
        data["BET_AMOUNT"] = bet_amount
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
        file.close()
