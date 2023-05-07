import csv
from random import *
import csv
import time
from colored import fg, bg, attr
from prettytable import from_csv
from guesses import game_play


def test_user_input(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'John Doe')
    user_name = str(input("Enter your Name: "))
    assert user_name == 'John Doe'

    monkeypatch.setattr('builtins.input', lambda _: '25')
    user_age = int(input("Enter your Age: "))
    assert user_age == 25


    



   
