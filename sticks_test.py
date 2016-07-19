import unittest
from sticks import *

def test_is_input_valid():
    assert is_input_valid(10) == 10
    assert is_input_valid('a') == False
    assert is_input_valid(8) == False

def test_has_friends():
    assert has_friends('N') == False
