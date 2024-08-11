"""
CP1404/CP5632 Practical
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


def format_sentence(phrase):
    """
    Format a phrase as a sentence, capitalizing the first letter and
    ensuring it ends with a single full stop.

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    phrase = phrase.capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should pass now that the function is fixed
    assert repeat_string("hi", 2) == "hi hi"

    # Testing Car class
    test_car_default_fuel = Car(name="DefaultCar")  # Test with the default fuel value
    assert test_car_default_fuel.fuel == 0, "Car does not set default fuel correctly"

    test_car_with_fuel = Car(name="FuelCar", fuel=10)  # Test with a specific fuel value
    assert test_car_with_fuel.fuel == 10, "Car does not set the given fuel correctly"

    # Run the doctests
    doctest.testmod()


# Run all the tests
run_tests()
