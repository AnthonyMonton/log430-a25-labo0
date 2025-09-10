"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "Calculatrice"

def test_addition():
    my_calculator = Calculator()
    resultat = my_calculator.addition(2, 3)
    assert resultat == 5
    assert my_calculator.last_result == 5

def test_subtraction():
    my_calculator = Calculator()
    resultat = my_calculator.subtraction(10, 4)
    assert resultat == 6
    assert my_calculator.last_result == 6

def test_multiplication():
    my_calculator = Calculator()
    resultat = my_calculator.multiplication(7, 6)
    assert resultat == 42
    assert my_calculator.last_result == 42

def test_division():
    my_calculator = Calculator()
    resultat = my_calculator.division(8, 2)
    assert resultat == 4
    assert my_calculator.last_result == 4

def test_division_by_zero():
    my_calculator = Calculator()
    resultat = my_calculator.division(5, 0)
    assert resultat == "Erreur : division par zéro"
    assert my_calculator.last_result == "Error"