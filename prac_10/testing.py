"""
CP1404 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # fix the repeat_string function above so that it passes the failing test
    #
    # test_car = Car()
    # assert test_car.odometer == 0, "Car does not set odometer correctly"

    # write assert statements to show if Car sets the fuel correctly

    # test_car = Car(fuel=10)
    # assert test_car.fuel == 10
    #
    # test_car = Car()
    # assert test_car.fuel == 0


# Write and test a function to format a phrase as a sentence

def format_phrase(user_input):
    """format phrase that user entered.
    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase('this function format phrase')
    'This function format phrase.'
    """
    user_input = input("Enter phrase:")
    sentence = user_input.capitalize()
    if sentence[-1] !='.':
       sentence += '.'
    return sentence

run_tests()

doctest.testmod()
