# Description: Dice class that allows for D4 - D100 sided dice to get rolled
#               and a function to create custom dice.
import random

# class Dice:
# """Allows you to roll dice d4 - d20"""


def d4(numdice):
    """D4 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 4)
    return total


def d6(numdice):
    """D6 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 6)
    return total


def d8(numdice):
    """D8 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 8)
    return total


def d10(numdice):
    """D10 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 10)
    return total


def d12(numdice):
    """D12 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 12)
    return total


def d20(numdice):
    """D20 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 20)

    return total


def d100(numdice):
    """D100 dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, 100)
    return total


def dx(numdice, sides):
    """DX dice"""
    total = 0
    for i in range(numdice):
        total += random.randint(1, sides)
    return total
