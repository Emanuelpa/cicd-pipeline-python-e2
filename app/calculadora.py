# app/calculadora.py

"""
DOCSTRING
"""

AUTORES = "???"


def sumar(a, b):
    """
    DOCSTRING
    """
    return a + b


def restar(a, b):
    """
    DOCSTRING
    """
    return a - b


def multiplicar(a, b):
    """
    DOCSTRING
    """
    return a * b


def dividir(a, b):
    """
    DOCSTRING
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
